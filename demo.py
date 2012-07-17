import petascore

# Basic developtment validation
getter = petascore.ResourceGetter()
resource = getter.get("http://www.metacritic.com/game/pc/fallout-new-vegas")
print resource.name
print resource.date
print resource.metascore
print resource.userscore
print resource.description
