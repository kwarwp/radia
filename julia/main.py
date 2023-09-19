# radia.julia.main.py
# autor Bruno
from _spy.vitollino.main import Cena, Elemento
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PEAO = "https://imgur.com/Z03KiRp.png"
class IlhaProibida:
	def __init__(self):
         oceano = Cena(IMAGEM).vai()
         portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit="Portao de Bronze",cena=oceano)
         palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, cena=oceano)
         peao = Elemento(PEAO, x=20, y=50, w=40, h=80, cena=oceano)
        
          
IlhaProibida()