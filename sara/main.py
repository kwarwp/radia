# radia.sara.main.py
# Fernanda - POO 2023 - UFRJ
#github.com/kwarwp
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 1000
IMAGEM = 'https://dinamicambiental.com.br/wp-content/uploads/2021/06/o-oceano-e-a-nossa-sobrevivencia.jpg'
PORTAO_BRONZE = 'https://thumbs.dreamstime.com/z/batedor-de-bronze-em-forma-uma-cabe%C3%A7a-le%C3%A3o-do-port%C3%A3o-da-catedral-col%C3%B4nia-na-alemanha-194660830.jpg?w=992'
PALACIO_CORAL = 'https://img.freepik.com/fotos-premium/palacio-subaquatico-com-ilustracao-colorida-de-ia-generativa-de-corais-e-peixes_268722-1554.jpg?w=740'
PEAO = 'https://imgur.com/zO3kiRp.png'
#Cena é classe e cena é atributo

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        #portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit='Portão de Bronze', cena=oceano)
        #palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, tit='Palácio de Coral', cena=oceano)
        #peao = Elemento(PEAO, x=20, y=70, w=80, h=80, tit='Palácio de Coral', cena=oceano)
        info_terrenos= [(10, PORTAO_BRONZE), (120, PALACIO_CORAL)]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px, local=lc)
        for px, lc in info_terrenos]
        self.peao = Peao(oceano)
        
class Terreno:
    def __init__(self, terreno, posx, posy, cena):
        self.terreno = Elemento(local, x=posx, y=posy, w=100, h=100, cena=cena)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PEAO, x=20, y=70, w=80, h= 80, cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.peao.x = 130


IlhaProibida()