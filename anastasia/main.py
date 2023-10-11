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

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Vanessa Vianna ** <vanessamvianna@ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

from _spy.vitollino.main import Cena, Elemento, STYLE #Cena C maiusculo porque é classe  Elemento peçinhas que colocam na cena 
#from julia.main import IlhaProibida as Ilha #importar o pacote julia módulo main, importar apenas a classe Ilha proibida e chamar de Ilha
#from julia import main as amain #importar o pacote todo julia main, chamar de amain
from array import array
import numpy as np

STYLE["width"] = 800 #a varios estilos, aqui selecionamos o widht 
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg" #IMAGEM DA INTERNET
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://img.freepik.com/fotos-premium/palacio-real-de-esplendor-arabe-islamico-em-um-pais-das-maravilhas-da-selva-tropical_865583-219.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

class IlhaProibida:  # : significa inicio de um bloco então posteriormente tem que estar intendado
    """
    Representa a classe principal do jogo
    Terrenos: Locais onde os peões podem ficar 
    """
    
    def __init__(self): #construcao, o primeiro parametro sempre se chama self - tabuleiro 
        self.oceano = oceano = Cena(IMAGEM).vai() #self.oceano é igual ao local oceano 
        #self.Terreno1 = Terreno(PORTAO_BRONZE, posx=10, posy=50, cena=oceano)
        #self.Terreno2 = Terreno(PALACIO_CORAL, posx=120, posy=50, cena=oceano)
        #info_terrenos= [(10,PORTAO_BRONZE), (120,PALACIO_CORAL),(230,PORTAO_BRONZE)] #PAR ORDENADOS
        #info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL]
        #info_terrenos = np.array([[0,1,0,1],[0,1,0,1],[0,1,0,1]])
        info_terrenos= [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px*110+10, local=lc)
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(self)
        self.terrenos[1].ocupa(self.peao) #chamou o terreno 1 e ocupa com o peão
        
    def direita(self, tereno):
        """Move o peão para a direita
        :param terreno: O terreno onde está o peão 
        :return
        """
        aqui = self.terrenos.index(terreno) #achar um terreno
        return self.terrenos[aqui+1]
                
class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h=100, 
        cena=cena)
        self.peao = None
        self.posx, self.posy = posx, posy
        
    def ocupa(self, peao):
        self.peao = peao #peao pertence a ele mesmo peao
        peao.mover(self.posx, self)
                               
class Peao:  
    """
    Marcador usado para definir a posição do jogador nos terrenos.
    """
    def __init__(self, ilha):
        """
        peao de posse da ilha
        """
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h=80,
        cena=ilha.oceano, vai=self.move) #PARAMETRO VAI CAPTURA O CLICK DO MOUSE E EXECUTA O MOVE 
        self.terreno = None
        self.ilha = ilha 
        #self.peao.vai = self.move outro modo de dizer vai=self.move
        
    def move_(self, ev=None):  # Corrigir: não está condizente!
        """
        qual o terreno a minha direta , ocupa.
        """
        terreno_destino = self.ilha.direita(0) #(self.terreno)
        self.peao.y = 300
        
    def move_(self, ev=None):  # Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(self.terreno)
        #self.peao.x = 170
        terreno_destino.ocupa(self)          
    def mover(self, x, terreno): 
        """
        movimento peão no terreno
        """
        self.terreno = terreno
        self.peao.x = x

        
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