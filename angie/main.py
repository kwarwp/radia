# radia.angie.main.py
from _spy.vitalline.main import Card, Elements, STYLE
STYLE["width"] = 800
STYLE["height"] = 600
IMAGEM = 'https://i.imgur.com/gVHmV2v.jpg'
PORTAO_BRONZE = 'https://i.imgur.com/8L6l87J.jpg'
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/z03kiRp.png"


class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10,y=10,
        w=100,h=100, cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=10, y=10, w=100, h=100, cena=oceano)
        peao = Elemento(PAWN, x=20, y=70, w=40, h=80, cena=oceano)
        self.peao = Peao(oceano)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PAWN, x=20, y=70, w=40, h=80, cena=oceano, vai=self.move)
    
    def move(self, ev=None):
        self.peao.x = 170
    
IlhaProibida()