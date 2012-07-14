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

# Unimplemented
class Result:
    def __init__(self):
        self.things = ""

# Contains info about the query to be made
class Query:
    def __init__(self):
        self.category = Category.GAME
        self.terms = "red+dead+redemption"
        self.baseurl = "http://www.metacritic.com/search/"
        self.finalurl = self.baseurl + "/game/" + self.terms + "/results"

    def __init__(self, category, terms):
        self.category = category
        self.terms = terms
        self.baseurl = "http://www.metacritic.com/search/"
        self.finalurl = self.baseurl + "/game/" + self.terms + "/results"
        
    def get_url(self):
        partialurl = {Category.ALL: self.baseurl + "all",
                  Category.MOVIE: self.baseurl + "movie",
                  Category.GAME: self.baseurl + "game",
                  Category.ALBUM: self.baseurl + "album",
                  Category.TV: self.baseurl + "tv",
                  Category.PERSON: self.baseurl + "person",
                  Category.TRAILER: self.baseurl + "trailer",
                  Category.COMPANY: self.baseurl + "company"}[self.category]
                  
        self.finalurl = partialurl + "/" + self.terms + "/results"
        return self.finalurl
    
query = Query(Category.GAME, "fallout")
print query.get_url()
   
        