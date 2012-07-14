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

class Scrapper():
    def __init__(self, query):
        self.raw_data = "Nothing yet"
        self.status_code = 0
        self.query = query
    
    def search(self):
        req = requests.get(self.query.get_url())
        self.status_code = req.status_code
        self.raw_data = req.content
    
query = Query(Category.GAME, "fallout")
print query.get_url()
scrapper = Scrapper(query)
scrapper.search()
print scrapper.status_code
   
        