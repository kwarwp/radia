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
from browser import document, window
from html.parser import HTMLParser

class Pokebot(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag in "h3":
            #procura a tag que define o nome da geração
            self.last = tag
            print("Encountered a start tag:", tag, attrs)
        if self.last == "h3" and tag == "span" and "mw-headline" in str(attrs):
            #self.pokedex[tag] = attrs[1][1] #(tag, attrs)
            self.gera = attrs[1][1]
            self.last = tag
        if tag in "img a":
            #self.pokedex[tag] = (tag, attrs)
            #print(str(attrs))
            if tag == "img":
                self.pokedex[self.last[1][1][1]] = self.gera
            else:
                if "'href', '/pt-br/wiki/" in  str(attrs):
                    self.last = (tag, attrs)


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag) if tag in "h3" else None

    def _handle_data(self, data):
        print("Encountered some data  :", data)
        
    def url_get(self, url):
        _fp = urllib.request.urlopen(url)
        return _fp.read()
        
    def geracao(self, gera):
        self.gera = gera
        
    def __init__(self):
        super().__init__()
        self.state = "h3 span"
        self.pokedex = {}
        self.gera = None
        self.last = None

        


        
        
if __name__ == "__main__":
    parser = Pokebot()
    #data = parser.url_get("https://pokemon.fandom.com/pt-br/wiki/Pok%C3%A9dex_Nacional")
    #parser.feed(data)
    parser.feed('''<html><head><title>Test</title></head>
<body><h1>Parse me!</h1><div id="xx"></div>
<h3><span id="Primeira_Gera.C3.A7.C3.A3o"></span><span class="mw-headline" id="Primeira_Geração">Primeira Geração</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a class="mw-editsection-visualeditor" title="Sign in to edit" href="https://auth.fandom.com/signin?redirect=https%3A%2F%2Fpokemon.fandom.com%2Fpt-br%2Fwiki%2FPok%25C3%25A9dex_Nacional%3Fveaction%3Dedit%26section%3D2&amp;uselang=pt-br" data-tracking-label="log-in-edit-section"><svg class="wds-icon wds-icon-tiny"><use xlink:href="#wds-icons-pencil-tiny"></use></svg></a><span class="mw-editsection-bracket">]</span></span></h3>
<table cellspacing="3" cellpadding="0" width="100%" style="margin: 0 0 1.7em 0; background: #ACD36C; border: 2px solid #537A13; font-size: 12px; color: #0E191A; border-radius: 15px; -moz-border-radius: 15px; -webkit-border-radius: 15px; -khtml-border-radius: 15px; -icab-border-radius: 15px; -o-border-radius: 15px;">
<tbody><tr>
<td width="100%" align="center">
<table cellpadding="6" width="100%" align="center" style="background: #80BB1D; border-radius: 11px; -moz-border-radius: 11px; -webkit-border-radius: 11px; -khtml-border-radius: 11px; -icab-border-radius: 11px; -o-border-radius: 11px;">

<tbody><tr>
<td width="12%" colspan="1" align="center" style="background: #ACD36C; line-height: 1.2; border-top-left-radius: 9px; -moz-border-radius-topleft: 9px; -webkit-border-top-left-radius: 9px; -khtml-border-top-left-radius: 9px; -icab-border-top-left-radius: 9px; -o-border-top-left-radius: 9px;"><span style="color: #537A13;"><b>Número</b></span>
</td>
<td width="50%" colspan="2" align="center" style="background: #ACD36C; line-height: 1.2;"><span style="color: #537A13;"><b>Pokémon</b></span>
</td>
<td width="38%" colspan="1" align="center" style="background: #ACD36C; line-height: 1.2; border-top-right-radius: 9px; -moz-border-radius-topright: 9px; -webkit-border-top-right-radius: 9px; -khtml-border-top-right-radius: 9px; -icab-border-top-right-radius: 9px; -o-border-top-right-radius: 9px;"><span style="color: #537A13;"><b>Tipo(s)</b></span>
</td></tr>
<tr>
<td align="center" class="modoclaroescuro" style="line-height: 1.2;">Nº 001
</td>
<td width="12%" align="center" class="modoclaroescuro" style="line-height: 1.2;"><a href="/pt-br/wiki/Bulbassauro" title="Bulbassauro"><img alt="001Bulbassauro" src="https://static.wikia.nocookie.net/pokepediabr/images/3/3c/001Bulbassauro.png/revision/latest/scale-to-width-down/50?cb=20210330173024&amp;path-prefix=pt-br" decoding="async" loading="lazy" width="50" height="50" data-image-name="001Bulbassauro.png" data-image-key="001Bulbassauro.png" data-relevant="1"></a>
</td>
<td width="43%" align="center" class="modoclaroescuro" style="line-height: 1.2;"><a href="/pt-br/wiki/Bulbassauro" title="Bulbassauro">Bulbassauro</a>
</td>
<td align="center" class="modoclaroescuro" style="line-height: 1.2;"><span style="background: #78C850; display: inline-block; border-radius: 5px; font-size: 10px; padding: 3px; width: 70px; line-height: 1.6; text-align: center;"><a href="/pt-br/wiki/Tipo_Grama" title="Tipo Grama"><font color="white">Grama</font></a></span> <span style="background: #A040A0; display: inline-block; border-radius: 5px; font-size: 10px; padding: 3px; width: 70px; line-height: 1.6; text-align: center;"><a href="/pt-br/wiki/Tipo_Venenoso" title="Tipo Venenoso"><font color="white">Venenoso</font></a></span>
</td></tr></table>
</body></html>''')
    print(parser.pokedex)
