# radia.grace.main.py
# __author__ Finn
from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"

IMAGEM = "https://i.imgur.com/my9MiVU.jpeg"

PORTAO_BRONZE = "https://i.imgur.com/103Lydz.png"
PALACIO_CORAL = "https://i.imgur.com/3Ywu4pe.jpg"
PALACIO_CORAL2 = "https://i.imgur.com/3Ywu4pe.jpg"
PALACIO_CORAL3 = "https://i.imgur.com/3Ywu4pe.jpg"
PALACIO_CORAL4 = "https://i.imgur.com/3Ywu4pe.jpg"

PAWN = "https://i.imgur.com/JKNaFSN.png"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PALACIO_CORAL2, PALACIO_CORAL3, PALACIO_CORAL4]
        
        self.terrenos = [Terreno(l, i * 120, 10, oceano) for i, l in enumerate(info_terrenos)]
        
        self.pawn = Peao(oceano)
        
        self.terrenos[2].ocupa(self.pawn)
        
class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.peao = None
        self.posx, self.posy = posx, posy
        self.local = Elemento(
            local, x=posx, y=posy, w=100, h=100, cena=oceano, vai=self.ocupa
        )
    
    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self.posy)
        
class Peao:
    def __init__(self, cena):
        self.pawn = Elemento(PAWN, x=10, y=10, w=100, h=100, cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.pawn.x = 120
        
    def mover(x, y):
        self.pawn.x = x
        self.pawn.y = y
        
IlhaProibida()