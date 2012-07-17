Petascore
=========
Python powered, web scraping based, Metacritic API

What is this?
-------------
A, for now, simple Python module that works as a Metacritic API. It uses the [BeautifulSoup][bs] and the [requests][requests] library.

How to use it
-------------
Copy-pasting from [demo.py](petascore/demo.py):
    
    // If you have included petascore.py in your project
    import petascore

    // For now Petascore just works with Metacritic URLs
    getter = petascore.ResourceGetter()
    resource = getter.get("http://www.metacritic.com/game/pc/fallout-new-vegas")

    print resource.name
    >> Fallout New Vegas
    print resource.date
    >> Oct 19, 2010
    print resource.metascore
    >> 84
    print resource.userscore
    >> 8.0
    print resource.description
    >> The latest game in the post-nuclear RPG series is being developed by many members of the Fallout 1 and 2  team at Obsidian Entertainment using the Fallout 3 engine.

License
-------
Petascore is released under the MIT License. See LICENSE for more details

**In development**
