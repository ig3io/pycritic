import pycritic

# Basic developtment validation
getter = pycritic.ResourceGetter()
resource = getter.get("http://www.metacritic.com/game/pc/fallout-new-vegas")
print resource.name
print resource.date
print resource.metascore
print resource.userscore
print resource.description
