# radia.pokebot.main.py
"""Robo para classificar Pokemon.

.. codeauthor:: Raphaella Freitas

Changelog
---------
.. versionadded::    23.10
    Usando o parser de html embutido (31).

|   **Open Source Notification:** This file is part of open source program **Pokemon Robot**
|   **Copyright © 2023  Raphaella Freitas**,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
"""

import urllib

from browser import document, window
from html.parser import HTMLParser

class Pokebot(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, attrs) if tag == "table" else None

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag) if tag == "table" else None

    def _handle_data(self, data):
        print("Encountered some data  :", data)
        
    def url_get(self, url):
        _fp = urllib.request.urlopen(url)
        return _fp.read()

        


        
        
if __name__ == "__main__":
    parser = Pokebot()
    #data = parser.url_get("https://pokemon.fandom.com/pt-br/wiki/Pok%C3%A9dex_Nacional")
    #parser.feed(data)
    parser.feed('''<html><head><title>Test</title></head>
<body><h1>Parse me!</h1><div id="xx"></div>
</body></html>''')
