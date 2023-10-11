# radia.alexa.main.py
# AA - Anderson Amorim (ouvinte)
from _spy.vitollino.main import Cena, Elemento, STYLE

IMAGEM = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fsegredosdomundo.r7.com%2Ffundo-do-mar-real%2F&psig=AOvVaw39wrJX08r73R0ivNIqbGqe&ust=1697032047707000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLDK_ZTP64EDFQAAAAAdAAAAABAFQ'
PORTAO_BRONZE = 'https://thumbs.dreamstime.com/z/batedor-de-bronze-em-forma-uma-cabe%C3%A7a-le%C3%A3o-do-port%C3%A3o-da-catedral-col%C3%B4nia-na-alemanha-194660830.jpg?w=992'
PALACIO_CORAL = 'https://img.freepik.com/fotos-premium/palacio-subaquatico-com-ilustracao-colorida-de-ia-generativa-de-corais-e-peixes_268722-1554.jpg?w=740'
VALE_TENEBROSO = 'http://2.bp.blogspot.com/-lo6Hr8UD4D4/T8FDTidezEI/AAAAAAAAAD0/4zitS77Hoxg/s1600/vale+da+sombra+da+morte.bmp'
PISTA = 'https://i0.wp.com/soepinaobasta.com/wp-content/uploads/2019/05/Heliponto.jpg?resize=1000%2C500&ssl=1'
PEAO = 'https://imgur.com/zO3kiRp.png'

STYLE["height"] = "6000px"
STYLE["width"] = 1000

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit='Portão de Bronze', cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, tit='Palácio de Coral', cena=oceano)
        peao = Elemento(PEAO, x=20, y=70, w=80, h=80, tit='Palácio de Coral', cena=oceano)
        info_terrenos= [PORTAO_BRONZE, PALACIO_CORAL, VALE_TENEBROSO, PISTA]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px*110+10, local=lc)
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(oceano)
        self.terrenos[2].ocupa(self.peao)
        
    def direita(self, terreno):
        aqui = self.terrenos.index(terreno)
        #return.self.terreno[aqui+1]
        
class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h=100, cena=cena)
        self.peao = None
        self.posx, self.posy = posx, posy
    
    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PEAO, x=20, y=70, w=80, h= 80, cena=oceano, vai=self.move)
        self.terreno = None
        self.ilha = ilha
        
    def move(self, ev=None):
        #self.peao.x = 130
        terreno_destino = self.ilha.direita(self.terreno)
        terreno_destino.ocupa(self)
        
    def mover(self, x, terreno):
        self.terreno = terreno
        self.peao.x = x



IlhaProibida()