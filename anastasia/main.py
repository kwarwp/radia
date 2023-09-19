# radia.anastasia.main.py
#_author_vanessa
print("alo")#escrito
from _spy.vitollino.main import Cena, Elemento, STYLE #Cena C maiusculo porque é classe  Elemento peçinhas que colocam na cena 
STYLE["width"] = 800 #a varios estilos, aqui selecionamos o widht 
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg" #COLOCAR IMAGEM DA INTERNET 
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PEAO = "https://imgur.com/zO3kiRp.jpg"



class IlhaProibida:  # : significa inicio de um bloco então posteriormente tem que estar intendado
    def __init__(self): #construcao, o primeiro parametro sempre se chama self
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, tit="Portão de Bronze", cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, tit="Palacio coral", cena=oceano)
        self.peao = Peao (oceano)

class Peao:  
    def __init__(self):
        peao = Elemento(PEAO, x=20, y=70, w=80, h=80, cena=oceano)
    def move(self, ev=None):
        self.peao.x = 170
    
IlhaProibida()