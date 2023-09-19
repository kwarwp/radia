# radia.roxanne.main.py
# __author__ Renan
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 800
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"


class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=50,
        w=100, h=100, tit="Portão de Bronze", cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, cena=oceano)


IlhaProibida()