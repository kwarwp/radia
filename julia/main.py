# radia.julia.main.pyhttp://supygirls.pythonanywhere.com/site/help.html
# autor Bruno
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 1000
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PEAO = "https://imgur.com/zO3kiRp.png"
class IlhaProibida:
	def __init__(self):
         oceano = Cena(IMAGEM).vai()
         portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit="Portao de Bronze",cena=oceano)
         palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, cena=oceano)
         self.peao = Peao(oceano)
class Peao:
    def __init__(self, oceano):
         peao = Elemento(PEAO, x=30, y=60, w=60, h=80, cena=oceano, vai=self.move)
        
    def move(self,ev=None):
            self.peao.x = 150
        
          
IlhaProibida()