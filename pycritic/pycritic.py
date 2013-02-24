import requests
import bs4

# It's "seems" a good idea to use this "enum", for now
class Category(object):
    ALL = 0
    MOVIE = 1
    GAME = 2
    ALBUM = 3
    TV = 4
    PERSON = 5
    TRAILER = 6
    COMPANY = 7

# Contains info about the query to be made
class Query(object):
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

# This class represents a generic resource found at Metacritic
class Resource(object):
    def __init__(self, name, date, category, metascore, userscore, description):
        self.name = name
        self.date = date
        self.category = category
        self.metascore = metascore
        self.userscore = userscore
        self.description = description


class Game(Resource):
    def __init__(self, name, date, category, metascore, userscore, description, platform):
        super.__init__(name, date, category, metascore, userscore, description)
        self.platform = platform


class Response(object):
    def __init__(self, status, content):
        self.status = status
        self.content = content

    def valid(self):
        return (self.status == 200)


class Browser(object):
    def get(self, url):
        request = requests.get(url)
        response = Response(request.status_code, request.content)
        return response


class Scraper(object):
    def __init__(self):
        self.browser = Browser()
        self.response = ""
        self.soup = ""

    def get(self, url):
        self.response = self.browser.get(url)
        self.soup = bs4.BeautifulSoup(self.response.content)
        return self.extract_data()

    def extract_data(self):
        name = self._extract_name()
        date = self._extract_date()
        category = self._extract_category()
        metascore = self._extract_metascore()
        userscore = self._extract_userscore()
        description = self._extract_description()
        resource = Resource(name, date, category, metascore, userscore, description)
        return resource

    def _extract_name(self):
        titles = self.soup.select(".product_title")
        title = titles[0].text
        info = title.split("\n")
        name = info[1].strip()
        return name

    def _extract_date(self):
        dates = self.soup.select(".release_data")
        date = dates[0].select(".data")[0].text.strip()
        return date

    def _extract_category(self):
        # TODO
        return Category.GAME

    def _extract_metascore(self):
        section = self.soup.select(".metascore_wrap")[0]
        score = section.select(".score_value")[0].text.strip()
        return int(score)

    def _extract_userscore(self):
        section = self.soup.select(".userscore_wrap")[0]
        score = section.select(".score_value")[0].text.strip()
        return float(score)

    def _extract_description(self):
        section = self.soup.select(".product_summary")[0].select(".data")[0]
        collapsed = section.select(".blurb_collapsed")
        description = ""
        if (collapsed):  # There's a collapse/expand button
            expanded = section.select(".blurb_expanded")
            description = unicode(collapsed[0].text + expanded[0].text).strip()
        else:
            description = unicode(section.text.strip())
        return unicode(description)
