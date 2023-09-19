# radia.roxanne.main.py
# __author__ Renan
from _spy.vitollino.main import Cena, Elemento
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"


class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)


IlhaProibida()