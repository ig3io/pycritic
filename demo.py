import pycritic

def print_resource_data(resource):
    print "Name: " + resource.name
    print "Release date: " + resource.date
    print "Metascore: " + str(resource.metascore)
    print "Userscore: " + str(resource.userscore)
    print "Description: " + resource.description

def main():
    scraper = pycritic.Scraper()
    alien = scraper.get("http://www.metacritic.com/movie/alien")
    print_resource_data(alien)
    aliens = scraper.get("http://www.metacritic.com/movie/aliens")
    print_resource_data(aliens)

if __name__ == "__main__":
    main()
