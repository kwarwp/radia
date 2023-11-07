

from _spy.vitollino.main import Cena, Elemento, STYLE
#from anastasia import main as amain
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"


class IlhaProibida:
    """ Representa a classe principal do Jogo.
    
    Terrenos 
        Locais onde os peões podem ficar.
        
    """
    def __init__(self):
        self.oceano = oceano = Cena(IMAGEM).vai()
        #self.terreno = Terreno(PORTAO_BRONZE, posx=10, posy=50,
        #cena=oceano)
        #self.terreno1 = Terreno(PALACIO_CORAL, posx=120, posy=50, cena=oceano)
        #info_terrenos= [(10, PORTAO_BRONZE), (120, PALACIO_CORAL), (230, PORTAO_BRONZE)]
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        self.peao = Peao(self)
        self.terrenos[1].ocupa(self.peao)
        
    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        matriz = [ [0,0,1,1,0,0], [0,1,1,1,1,0], [1,1,1,1,1,1], [1,1,1,1,1,1], [0,1,1,1,1,0], [0,0,1,1,0,0]]
        info_terrenos= [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL] * 9
        py=50;
        px=1;
        for i in range(6):
            for j in range(6):
                if matriz[i][j] == 1:
                    self.terrenos = [Terreno(local=info_terrenos[i*j], posy=py, posx=px*110+10,cena=oceano)]
                px = px+1
            py = py + 110
            px = 1
                    
        
    def direita(self, terreno):
        """ Move o peão para a direita.
        
        :param terreno: O terreno onde está o peão
        :return: O terreno onde o peão vai
        """
        aqui = self.terrenos.index(terreno)
        return self.terrenos[aqui+1]

class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h= 100, cena=cena, vai=self.ocupa)
        self.peao = None
        self.posx, self.posy = posx, posy
        
    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)

class Peao:
    """ Marcador usado para definir a posição do jogador nos terrenos.
    """
    def __init__(self, ilha):
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h= 80,
        cena=ilha.oceano, vai=self.move)
        self.terreno = None
        self.ilha = ilha
        #self.peao.vai = self.move
        
    def move_(self, ev=None):  # Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(0) #(self.terreno)
        self.peao.y = 300
        
    def move(self, ev=None):  # Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(self.terreno)
        #self.peao.x = 170
        terreno_destino.ocupa(self)        
    def mover(self, x, terreno):
        self.terreno = terreno
        self.peao.x = terreno.posx

        
if __name__ == "__main__": 
    #print((amain.__name__))
    ##import antigravity as ag
    #from __future__ import braces
    import __phello__
    #ag.fly()
    
    IlhaProibida()
    #IlhaProibida()