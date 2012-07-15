import requests
import lxml

# It's "seems" a good idea to use this "enum", for now
class Category:
    ALL = 0
    MOVIE = 1
    GAME = 2
    ALBUM = 3
    TV = 4
    PERSON = 5
    TRAILER = 6
    COMPANY = 7

# Contains info about the query to be made
class Query:
    # Standard constructor (w/ parameters)
    def __init__(self, category, terms):
        self.category = category
        self.terms = terms
        self.base_url = "http://www.metacritic.com/search/"
        partial_url = {Category.ALL: self.base_url + "all",
                  Category.MOVIE: self.base_url + "movie",
                  Category.GAME: self.base_url + "game",
                  Category.ALBUM: self.base_url + "album",
                  Category.TV: self.base_url + "tv",
                  Category.PERSON: self.base_url + "person",
                  Category.TRAILER: self.base_url + "trailer",
                  Category.COMPANY: self.base_url + "company"}[self.category]
        self.url = partial_url + "/" + terms + "/results"
        
    # Returns the URL of the created query
    def get_url(self):
        return self.url

# This class represents a generic resource found at Metascore, identified by
# its URL
class Resource:
    def __init__(self, url):
        self.url = url
        self.get_data(url)
        
    def get_data(self):
        req = requests.get(self.url)
        if (req.status_code != 200):
            # Something went wrong
            return False
        raw_data = req.content
        # Parsing magic goes here!        
        self.name = "..."
        self.metascore = 0
        self.userscore = 0
        self.description = "..."
    

# This will be the main scrapping class. Its objective is to allow the
# programmer to search directly through the Petascore module
class Searcher():
    def __init__(self, query):
        self.raw_data = "Nothing yet"
        self.status_code = 0
        self.query = query
    
    def search(self):
        req = requests.get(self.query.get_url())
        self.status_code = req.status_code
        self.raw_data = req.content
        
    # def get_results(self):
    #     ...
    #     return infor about the results
    
    # def get_result_at(self, index);
    #     ...
    #     return some_url
    
    # ...
    
# Basic development validation
query = Query(Category.GAME, "fallout")
print query.get_url()
scrapper = Searcher(query)
scrapper.search()
print scrapper.status_code
        