# radia.julia.main.py
# autor Bruno
from _spy.vitollino.main import Cena, Elemento
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PEAO = "https://img2.gratispng.com/20180222/udq/kisspng-chess-piece-pawn-white-and-black-in-chess-white-chess-pawn-soldiers-5a8e9826b0cc02.1523795815192945027242.jpg"

class IlhaProibida:
	def __init__(self):
         oceano = Cena(IMAGEM).vai()
         portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit="Portao de Bronze",cena=oceano)
         palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, cena=oceano)
         palacio = Elemento(PEAO, x=330, y=50, w=100, h=100, cena=oceano)
        
          
IlhaProibida()