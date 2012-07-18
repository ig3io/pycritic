import pycritic

def print_resource_data(resource):
    print "Name: " + resource.name
    print "Release date: " + resource.date
    print "Metascore: " + str(resource.metascore)
    print "Userscore: " + str(resource.userscore)
    print "Description: " + resource.description


getter = pycritic.ResourceGetter()
alien = getter.get("http://www.metacritic.com/movie/alien")
print_resource_data(alien)
aliens = getter.get("http://www.metacritic.com/movie/aliens")
print_resource_data(aliens)

