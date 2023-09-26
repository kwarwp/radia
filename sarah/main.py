# radia.sarah.main.py
# __author__ Filipe
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"


class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        self.terreno = Terreno(PORTAO_BRONZE, posx=10, posy=50,
        cena=oceano)
        self.terreno1 = Terreno(PALACIO_CORAL, posx=120, posy=50, cena=oceano)
        info_terrenos= [(10, PORTAO_BRONZE), (120, PALACIO_CORAL)]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px, local=lc)
        for px, lc in info_terrenos]
        self.peao = Peao(oceano)

class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h= 100,
        cena=cena)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h= 80,
        cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.peao.x = 170
        

IlhaProibida()