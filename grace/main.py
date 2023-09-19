# radia.grace.main.py
# __author__ Finn
from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"

IMAGEM = "https://i.imgur.com/my9MiVU.jpeg"
PORTAO_BRONZE = "https://i.imgur.com/103Lydz.png"
PALACIO_CORAL = "https://i.imgur.com/3Ywu4pe.jpg"

PAWN = "https://static.vecteezy.com/system/resources/previews/021/975/110/original/pawn-3d-render-icon-illustration-with-transparent-background-chess-game-png.png"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=10, w=100, h=100, cena=oceano)
        
        pawn = Elemento(PAWN, x=10, y=10, w=100, h=100, cena=oceano)
        
IlhaProibida()