# radia.roxanne.main.py
# __author__ Carlo
"""Página de entrada do jogo Ilha Proibida.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.10
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

from _spy.vitollino.main import Cena, Elemento, STYLE
from julia.main import IlhaProibida as Ilha
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
        info_terrenos= [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx=px*110+10, local=lc)
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(self)
        self.terrenos[1].ocupa(self.peao)
        
    def direita(self, terreno):
        """ Move o peão para a direita.
        
        :param terreno: O terreno onde está o peão
        :return: O terreno onde o peão vai
        """
        aqui = self.terrenos.index(terreno)
        return self.terreno[aqui+1]

class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h= 100,
        cena=cena)
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
        
    def move(self, ev=None):  # Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(self.terreno)
        #self.peao.x = 170
        terreno_destino.ocupa(self)        
    def mover(self, x, terreno):
        self.terreno = terreno
        self.peao.x = x

        
if __name__ == "__main__": 
    print(help(Ilha))
    #IlhaProibida()