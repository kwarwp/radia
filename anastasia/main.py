# radia.anastasia.main.py
#_author_vanessa
print("alo")#escrito
from _spy.vitollino.main import Cena, Elemento, STYLE #Cena C maiusculo porque é classe  Elemento peçinhas que colocam na cena 
STYLE["width"] = 800 #a varios estilos, aqui selecionamos o widht 
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg" #COLOCAR IMAGEM DA INTERNET 
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

class IlhaProibida:  # : significa inicio de um bloco então posteriormente tem que estar intendado
    def __init__(self): #construcao, o primeiro parametro sempre se chama self - tabuleiro 
        self.oceano = ocenao = Cena(IMAGEM).vai() #self.oceano é igual ao local oceano 
        #self.Terreno1 = Terreno(PORTAO_BRONZE, posx=10, posy=50, cena=oceano)
        #self.Terreno2 = Terreno(PALACIO_CORAL, posx=120, posy=50, cena=oceano)
        #info_terrenos= [(10,PORTAO_BRONZE), (120,PALACIO_CORAL),(230,PORTAO_BRONZE)] #PAR ORDENADOS
        info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px*110+10, local=lc) 
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(self)
        self.terrenos[2].ocupa(self.peao) #chamou o terreno 1 e ocupa com o peão
        
    def direita(self, tereno):
        self.terrenos.index(terreno)
        return self.terreno[aqui+1] 
        
        
class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h=100, 
        cena=cena)
        self.peao = None
        self.posx, self.posy = posx, posy
        
    def ocupa(self, peao):
        self.peao = peao #peao pertence a ele mesmo peao
        peao.mover(self.posx, terreno)
        
                       
class Peao:  
    def __init__(self, ilha): #peao de posse da ilha 
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h=80,
        cena=ilha.oceano, vai=self.move) #PARAMETRO VAI CAPTURA O CLICK DO MOUSE E EXECUTA O MOVE 
        self.terreno = mone
        self.ilha = ilha 
        
    def move(self, ev=None):  # Corrigir: não condizente! 
        terreno_destino = self.ilha.direita(self.terreno) 
        self.peao.x = 170
        
    def mover(self, x, terreno): #movimento peão no terreno
        self.terreno = terreno
        self.peao.x = x 
        
IlhaProibida()