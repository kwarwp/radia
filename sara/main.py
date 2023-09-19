# radia.sara.main.py
# Fernanda - POO 2023 - UFRJ
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 1000
STYLE["height"] = 800
IMAGEM = 'https://dinamicambiental.com.br/wp-content/uploads/2021/06/o-oceano-e-a-nossa-sobrevivencia.jpg'
PORTAO_BRONZE = 'https://thumbs.dreamstime.com/z/batedor-de-bronze-em-forma-uma-cabe%C3%A7a-le%C3%A3o-do-port%C3%A3o-da-catedral-col%C3%B4nia-na-alemanha-194660830.jpg?w=992'
PALACIO_CORAL = 'https://img.freepik.com/fotos-premium/palacio-subaquatico-com-ilustracao-colorida-de-ia-generativa-de-corais-e-peixes_268722-1554.jpg?w=740'
PEAO = 'https://o.remove.bg/downloads/d883708e-8e09-49b7-9bad-f1c634272eb2/kisspng-chess-piece-pawn-king-queen-painted-black-chess-pieces-5a80da4ed471c4.3075899115183939348702-removebg-preview.png'
#Cena é classe e cena é atributo

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit='Portão de Bronze', cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, tit='Palácio de Coral', cena=oceano)
        peao = Elemento(PEAO, x=20, y=70, w=90, h=60, tit='Palácio de Coral', cena=oceano)
        self.peao = Peao(oceano)
        
class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PEAO, x=20, y=70, w=90, h=60, tit='Palácio de Coral', cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.peao.x = 170

IlhaProibida()