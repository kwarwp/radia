# radia.anastasia.main.py
#_author_vanessa
"""Página de entrada do jogo Ilha Proibida.

.. codeauthor:: Vanessa Vianna <vanessamvianna@ufrj.br>

Changelog
---------
.. versionadded::    23.10
    Versão Inicial (1).
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (2).
    
.. versionadded::    10.10
    Versão Inicial (3).
    documentacao das classes, help 
    
.. versionadded::    24.10
    Versão Inicial (4).
    montagem do tabuleiro, movimentação do peao 


.. versionadded::    31.10
    Versão Inicial (5).
    movimentação do peao - apenas em x ou y e nao na diagonal
    double dispatch
    colocação de título nas imagens 
    sorteio dos terrenos 
    elemento nos terrenos
  
    
    

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Vanessa Vianna ** <vanessamvianna@ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

"""
importacao de modulos
Cena C maiusculo porque é classe  
Elemento pecinhas que colocam na cena 
collections, namedtuple: criar classe em uma linha
"""
from _spy.vitollino.main import Cena, Elemento, STYLE 
from collections import namedtuple
Ter = namedtuple("Ter", "nome imagem tafv") #classe Ter - par ordenado que eu nomeio cada um. criar parametros com os itens divididos por espaço

"""
IMAGENS
"""
STYLE["width"] = 800 #a varios estilos, aqui selecionamos o widht 
STYLE["height"] = "800px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"
TAFVS = "KXZXTei LK4p1xG rUNsKEH qp5Zbn8".split()
NOMES = ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
"PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
"TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
"PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()
LINKS = ("CU3TLYh BL6lB7H tLDbzd2 OZE1myn J6ow4jR v0g7eGm 45aU3nf "
"yKU6ngz sdJ4W5O pjVcyoy ZNuPWqZ O0OSVFt "
"J160xpm 2j1IAyf b4xtltc E9MflTP NDioDZg TCmLjeT "
"rYxQaTa MvN7kTU Uni02EK cG5UYCf GC8V8CQ 7o1qq10").split()

#instancia com argumentos de Ter

    



class IlhaProibida:  #significa inicio de um bloco então posteriormente tem que estar intendado
    """
    Representa a classe principal do jogo
    Terrenos: Locais onde os peões podem ficar 
    MONTAGEM DO JOGO
    """
    
    def __init__(self): #construcao, o primeiro parametro sempre se chama self - tabuleiro 
        self.oceano = oceano = Cena(IMAGEM).vai() #self.oceano é igual ao local oceano 
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        self.peao = Peao(self)
        self.peao.mover(self.terrenos[0])
     

    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        from random import shuffle
        tafv = [None]*16+TAFVS*2
        info_terrenos = it = [Ter(nome=NOMES.pop(0), imagem=LINKS.pop(0), 
        tafv=tafv.pop()) for _ in range(24)] #Agora info_terrenos é uma lista de Ter #pop elimina o último
        #info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL] * 9
        suffle(info_terrenos)
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=it.pop(0), ilha=self)
                         for px in range(36) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        self.terrenos[4].afundar()

    def desocupa_e_vai_para(self, terreno_destino):
        self.peao.move(terreno_destino)     

    def direita(self, terreno):
        """Move o peão para a direita
        :param terreno: O terreno onde está o peão 
        :return: O terreno onde o peão vai
        """
        aqui = self.terrenos.index(terreno) #achar um terreno
        return self.terrenos[aqui + 1]
                
class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """
    def __init__(self, local: Ter, posx, posy, cena, ilha): #Ter anotação, tem que passar aqui um cara ter
        #img = local.imagem
        img = f"https://imgur.com/{local.imagem}.jpg"
        self.local = Elemento (img, x=posx * 110 + 10, y=posy * 110 + 50, w=100, h=100,
                              cena=cena)
        estilo = {'background-color': '#343', 'color': 'white'}
        letreiro = Elemento("", w=100, h=20, style=estilo, cena=self.local)
        letreiro.elt.text = local.nome
        tafv = Elemento(local.tafv, w=30, h=30, style=estilo, cena=self.local)
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
        def contiguos(origem, destino): #mover verificar direçao se esta no sentido x e no sentido y 
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
    """
    Marcador usado para definir a posição do jogador nos terrenos.
    :param ilha: Referência ao tabuleiro.
    """
    def __init__(self, ilha):
        """
        peao de posse da ilha
        """
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h=80, #elemento vai por cima da cena 
                             cena=ilha.oceano) #PARAMETRO VAI CAPTURA O CLICK DO MOUSE E EXECUTA O MOVE 
        self.terreno = ilha # era None, mas o peão agora nasce na ilha
        self.ilha = ilha 
        #self.peao.vai = self.move outro modo de dizer vai=self.move
      
        
    def move_(self, terreno):  # Corrigir: não está condizente!
        """
        qual o terreno a minha direta , ocupa.
        """
        sef.terreno = terreno
        terreno.peao = self
        self.peao.x, self.peao.y = terreno.posx * 110 + 10, terreno.posy * 110 + 50
          
    def mover(self, terreno_destino): 
        """
        movimento peão no terreno
        """
        self.terreno.desocupa_e_vai(terreno_destino) 
       
if __name__ == "__main__": #troca o name pelo main 
    """
    O nome do ambiente principal do programa,pode ser verificado usando a expressão
    o help busca a documentação e o print mostra essa documentação
    """
    #print (help(Peao))
    #print((amain.__name__)) este comando mostra o nome do módulo importado no caso anastasia.main   
    #print((amain.__name__))
    ##import antigravity as ag
    #from __future__ import braces
    #import __phello__
    #ag.fly()
    
    
    IlhaProibida()
    ata = Ter(nome="atalaia", imagem='imgur/xyz', tafv=None)