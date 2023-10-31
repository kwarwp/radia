# radia.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from collections import namedtuple
Ter = namedtuple("Ter", "nome imagem tafv")
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

TFAVS = "KXZXTei LK4p1xG rUNsKEH qp5Zbn8".split()

NOMES = ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
"PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
"TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
"PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()
LINKS = ("CU3TLYh BL6lB7H tLDbzd2 OZE1myn J6ow4jR v0g7eGm 45aU3nf "
"yKU6ngz sdJ4W5O pjVcyoy ZNuPWqZ O0OSVFt "
"J160xpm 2j1IAyf b4xtltc E9MflTP NDioDZg TCmLjeT "
"rYxQaTa MvN7kTU Uni02EK cG5UYCf GC8V8CQ 7o1qq10").split()


class IlhaProibida:
    """ Representa a classe principal do Jogo.
    
    Terrenos 
        Locais onde os peões podem ficar.
        
    """

    def __init__(self):
        self.oceano = Cena(IMAGEM).vai()
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        self.peao = Peao(self)
        self.peao.mover(self.terrenos[0])

    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        from random import shuffle
        # Agora info_terrenos será uma lista de Ter -> Como criar?
        info_terrenos = []
        for terreno, link in zip(NOMES, LINKS):
            info_terrenos.append(("https://imgur.com/" + link, terreno))
        shuffle(info_terrenos)
        # Cada terreno realmente criado "puxa" um terreno da lista de "Ter's
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=lc[0], ilha=self)
                         for px, lc in enumerate(info_terrenos) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        self.terrenos[4].afundar()

    def desocupa_e_vai_para(self, terreno_destino):
        self.peao.move(terreno_destino)

    def direita(self, terreno):
        """ Move o peão para a direita.
        
        :param terreno: O terreno onde está o peão
        :return: O terreno onde o peão vai
        """
        aqui = self.terrenos.index(terreno)
        return self.terrenos[aqui + 1]


class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, local: Ter, posx, posy, cena, ilha):
        #img = local.imagem
        #self.local = Elemento(img
        self.local = Elemento(local, x=posx * 110 + 10, y=posy * 110 + 50, w=100, h=100,
                              cena=cena)
        estilo = {'background-color': 'slategray', 'color': 'white'}
        letreiro = Elemento("", w=100, h=20, style=estilo, cena=self.local)
        letreiro.elt.text = lc[1]
        #tafv = Elemento(local.tafv, ....)
        self.peao, self.ilha = None, ilha
        self.posx, self.posy = posx, posy
        self.local.vai = self.vai
        self.afunda = False

    def vai(self, _=0):
        self.ilha.peao.mover(self)

    def afundar(self):
        self.afunda = True
        self.local.o = 0.2

    def desocupa_e_vai_para(self, terreno_destino):
        def contiguos(origem, destino):
            if not origem:
                return True
            from operator import xor
            return xor(abs(origem.posx - destino.posx) == 1,
            abs(origem.posy - destino.posy) == 1) and not destino.afunda

        peao_pode_ir = contiguos(self, terreno_destino)
        # executar o movimento do peão agora que foi autorizado pelo pode ir
        self.peao.move(terreno_destino) if peao_pode_ir else None

    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)


class Peao:
    """ Marcador usado para definir a posição do jogador nos terrenos.
        
        :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, ilha):
        """
        """
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h=80,
                             cena=ilha.oceano)
        self.terreno = ilha  # era None, mas o peão agora nasce na ilha
        self.ilha = ilha

    def move(self, terreno):  # Corrigir: não está condizente!
        self.terreno = terreno
        terreno.peao = self
        self.peao.x, self.peao.y = terreno.posx * 110 + 10, terreno.posy * 110 + 50

    def mover(self, terreno_destino):
        self.terreno.desocupa_e_vai_para(terreno_destino)


if __name__ == "__main__":
    # IlhaProibida()
    IlhaProibida()
    info_terrenos = []
    for terreno, link in zip(NOMES, LINKS):
        info_terrenos.append(("https://imgur.com/" + link, terreno))
    print(info_terrenos)
    print(len(info_terrenos))
    #ata = Ter(nome="atalaia", imagem='imgur/xyz', tafv=None)
    #ata.nome = "pista"
    #print(ata.nome, ata.tafv)
    # print([(px, int(abs(2.5-px//6))) for px in range(36)])
