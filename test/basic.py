import pycritic

def print_resource_data(resource):
    if resource is None:
        print "Link not valid"
    else:
        print "Name: " + str(resource.name)
        print "Platform: " + str(resource.platform)
        print "Release date: " + str(resource.date)
        print "Metascore: " + str(resource.metascore)
        print "Userscore: " + str(resource.userscore)
        print "Description: " + resource.description #Dont use str for description Unicode-ASCII issues

def main():
    scraper = pycritic.Scraper()
    alien = scraper.get("http://www.metacritic.com/movie/alien")
    print_resource_data(alien)
    aliens = scraper.get("http://www.metacritic.com/movie/aliens")
    print_resource_data(aliens)
    fallout = scraper.get("http://www.metacritic.com/game/pc/fallout-new-vegas")
    print_resource_data(fallout)

def search_meta():
    scraper = pycritic.Scraper()
    query = pycritic.Query(pycritic.Category.GAME,"Guacamelee! Super Turbo Championship Edition")
    search_results=query.get()  #returns a list of URLs

    for link in search_results:
        details=scraper.get(link)
        print "URL: " + link
        print_resource_data(details)


if __name__ == "__main__":
    main()
    search_meta()
