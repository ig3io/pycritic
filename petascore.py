import requests
import lxml

class Category:
    ALL = 0
    MOVIE = 1
    GAME = 2
    ALBUM = 3
    TV = 4
    PERSON = 5
    TRAILER = 6
    COMPANY = 7

class ResultList:
    

def check():
    req = request.get("http://google.com")
    if (req.status_code == 200):
        return "OK"
    else:
        return "Oops"

print check()
