Pycritic
=========
Python powered, web scraping based, Metacritic API

What is this?
-------------
A simple Python module that works as a Metacritic API. It uses the [BeautifulSoup][bs] and the [Requests][requests] library.

Pycritic is under development and hasn't been tested enough (just in Python 2.7.3 for now).

Comming Soon (tm)
-----------------
* Support for all categories
* Search

How to use it
-------------
Based on [demo.py][demo.py]:

```python
# If you have included pycritic.py in your project
import pycritic

# For now Pycritic just works with Metacritic URLs
scraper = pycritic.Scraper()
scraper = scraper.get("http://www.metacritic.com/game/pc/fallout-new-vegas")

print resource.name
# >> Fallout New Vegas
print resource.date
# >> Oct 19, 2010
print resource.metascore
# >> 84
print resource.userscore
# >> 8.0
print resource.description
# >> The latest game in the post-nuclear RPG series is being developed by many members of the Fallout 1 and 2  team at Obsidian Entertainment using the Fallout 3 engine.
```

License
-------
Pycritic is released under the MIT License. See [LICENSE][license] for more details

[requests]: http://docs.python-requests.org/en/latest/index.html
[bs]: http://www.crummy.com/software/BeautifulSoup/
[demo.py]: https://github.com/ignaciocontreras/pycritic/blob/master/demo.py
[license]: https://github.com/ignaciocontreras/pycritic/blob/master/LICENSE
