# radia.sarah.main.py
# __author__ Filipe Marçal
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
HELICOPTERO = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/LAPD_Bell_206_Jetranger.jpg/450px-LAPD_Bell_206_Jetranger.jpg"
PANTANO = "https://cdn.pixabay.com/photo/2015/07/15/01/09/sunset-845552_1280.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"
BOSQUE = "https://cdn.pixabay.com/photo/2018/04/06/00/25/trees-3294681_1280.jpg"


class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        self.terreno = Terreno(PORTAO_BRONZE, posx=10, posy=50, cena=oceano)
        self.terreno1 = Terreno(PALACIO_CORAL, posx=120, posy=50, cena=oceano)
        self.terreno2= Terreno(HELICOPTERO, posx=10, posy=170, cena=oceano)
        self.terreno3 = Terreno(PALACIO_CORAL, posx=120, posy=170, cena=oceano)
        self.terreno4 = Terreno(PANTANO, posx=230, posy= 170, cena=oceano)
        self.terreno5 = Terreno(BOSQUE, posx=340, posy=170, cena=oceano)
        self.terreno6 = Terreno(PANTANO, posx=10, posy= 290, cena=oceano)
        self.terreno7 = Terreno(BOSQUE, posx=120, posy=290, cena=oceano)
        info_terrenos= [(10, PORTAO_BRONZE), (120, PALACIO_CORAL), (230, PORTAO_BRONZE)]
        info_terrenos= [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px*110+10, local=lc)
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(oceano)
        self.terrenos[2].ocupa(self.peao)

class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h= 100,
        cena=cena)
        self.peao = None
        self.posx, self.posy = posx, posy
        
    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h= 80,
        cena=oceano, vai=self.move)
        self.terreno = None
        
    def move(self, ev=None):  # Corrigir: não está condizente!
        self.peao.x = 170
        
    def mover(self, x, terreno):
        self.terreno = terreno
        self.peao.x = x

        

IlhaProibida()