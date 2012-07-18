import pycritic


getter = pycritic.ResourceGetter()
resource = getter.get("http://www.metacritic.com/movie/aliens")
print resource.name
print resource.date
print resource.metascore
print resource.userscore
print resource.description
