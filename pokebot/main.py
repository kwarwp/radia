# radia.pokebot.main.py
import urllib.request

from browser import document, window


def create_script_tag(src):
    _fp = urllib.request.urlopen(src)
    _data = _fp.read()

    _tag = document.createElement('script')
    _tag.type = "text/javascript"
    _tag.text = _data
    document.get(tag='head')[0].appendChild(_tag)
    

class Pokebot:
    def __init__(self):
        create_script_tag("https://cdn.jsdelivr.net/npm/puppeteer@21.4.1/lib/cjs/puppeteer/puppeteer.min.js")
        ppp = window.puppeteer
        
        
if __name__ == "__main__":
    Pokebot()
