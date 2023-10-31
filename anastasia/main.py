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
    movimentação do peao - apenas em um e nao na diagonal - double dispatch 
  
    
    

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Vanessa Vianna ** <vanessamvianna@ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

"""
importacao de diretorio / biblioteca
"""
from _spy.vitollino.main import Cena, Elemento, STYLE #Cena C maiusculo porque é classe  Elemento pecinhas que colocam na cena 
#from julia.main import IlhaProibida as Ilha #importar o pacote julia módulo main, importar apenas a classe Ilha proibida e chamar de Ilha
#from julia import main as amain #importar o pacote todo julia main, chamar de amain
#from array import array
#import numpy as np
import random # Importa o módulo random do Python

"""
IMAGENS
"""
STYLE["width"] = 800 #a varios estilos, aqui selecionamos o widht 
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png" #PINO
OBSERVATORIO = "https://imgur.com/J5fn5ZX" #OBSERVATORIO
BOSQUE = "https://imgur.com/1LoY0Bf" #BOSQUE



class IlhaProibida:  # : significa inicio de um bloco então posteriormente tem que estar intendado
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
        info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL] * 9
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=lc, ilha=self)
                         for px, lc in enumerate(info_terrenos) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        self.terrenos[4].afundar()
        ]
        #random.shuffle(info_terrenos) #Embaralha a lista de cartas (tabuleiro)
        #tabuleiro = [i for i in range(1, 24)] #Gera uma lista de cartas com números de 1 a 24, representando as cartas
        #for i in range(1): #sorteia 1 vez, 2 cartas  
            #print(info_terrenos[i:i+2]) 
        #for i in range(1): #sorteia 1 vez, 4 cartas  
            #print(info_terrenos[i:i+4]) 
        #for i in range(2): #sorteia 2 vezes, 6 cartas  
            #print(info_terrenos[i:i+6]) 
        #for i in range(1): #sorteia 1 vez, 4 cartas  
            #print(info_terrenos[i:i+4]) 
        #for i in range(1): #sorteia 1 vez, 2 cartas  
            #print(info_terrenos[i:i+2]) 
        #info_terrenos = self.sprite("terreno", 0, 0)
        #info_terrenos.frame = 2  # este número seleciona o ladrilho que vai ser colocado
        #info_terrenos = self.sprite("terreno", 0, 0)
        #info_terrenos.frame = 4  # este número seleciona o ladrilho que vai ser colocado
        #info_terrenos = self.sprite("terreno", 0, 0)
        #info_terrenos.frame = 6  # este número seleciona o ladrilho que vai ser colocado
        #info_terrenos = self.sprite("terreno", 0, 0)
        #info_terrenos.frame = 4  # este número seleciona o ladrilho que vai ser colocado
        #info_terrenos = self.sprite("terreno", 0, 0)
        #info_terrenos.frame = 2  # este número seleciona o ladrilho que vai ser colocado
    def desocupa_e_vai_para(self, terreno_destino):
        self.peao.move(terreno_destino)     
       
    def direita(self, terreno):
        """Move o peão para a direita
        :param terreno: O terreno onde está o peão 
        :return
        """
        aqui = self.terrenos.index(terreno) #achar um terreno
        return self.terrenos[aqui+1]
                
class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """
    def __init__(self, local, posx, posy, cena, ilha):
        self.local = Elemento(local, x=posx * 110 + 10, y=posy * 110 + 50, w=100, h=100,
                              cena=cena)
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
            return abs(origem.posx - destino.posx) <= 1 and abs(origem.posy - destino.posy) <= 1

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
    def __init__(self, ilha, frame, x, y):
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
          
    def mover(self, x, terreno_destino): 
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