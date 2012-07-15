import requests
import bs4

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

# This will be the main scraping class. Its objective is to allow the
# programmer to search directly through the Petascore module
class Searcher:
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


# This class represents a generic resource found at Metascore, identified by
# its URL
class Resource:
    def __init__(self):
        self.url = ""
        self.name = ""
        self.extra = ""
        self.category = Category.ALL
        self.metascore = 0
        self.userscore = 0
        self.description = ""

def get_resource(url):
    fail = False
    success = True
    req = requests.get(url)
    if (req.status_code != 200):
        return fail
    soup = bs4.BeautifulSoup(req.content)
    titles = soup.select(".product_title")
    title = titles[0].text
    info = title.split("\n")
    resource = Resource()
    resource.name = info[1].strip()
    resource.extra = info[2].strip()
    return success, resource
    
# Basic Query/Searcher development validation
query = Query(Category.GAME, "fallout+3")
print query.get_url()
searcher = Searcher(query)
searcher.search()
print searcher.status_code
        
# Basic Resource/get_resource developtment validation
success, resource = get_resource("http://www.metacritic.com/game/pc/fallout-3")
if (success == True):
    print resource.name
    print resource.extra
else:
    print "Something went wrong"