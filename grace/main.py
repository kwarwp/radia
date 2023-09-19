# radia.grace.main.py
# __author__ Finn
from _spy.vitollino.main import Cena, Elemento

print("TEST")

IMAGEM = "https://imgur.com/a/cJCkxeA.jpg"
PORTAO_BRONZE = "https://imgur.com/103Lydz"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        #portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        
IlhaProibida()