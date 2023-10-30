# radia.danae.main.py
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
from collections import namedtuple

STYLE["width"] = 800
STYLE["height"] = "600px"
LADO = 85
PORTA_OURO = "https://i.imgur.com/PvkZSQP.jpg"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
TFAV = "https://i.imgur.com/VivubQG.png"
TFAVS = "KXZXTei LK4p1xG rUNsKEH qp5Zbn8".split()
NOMES = ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
"PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
"TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
"PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()
LINKS = ("CU3TLYh BL6lB7H tLDbzd2 OZE1myn J6ow4jR v0g7eGm 45aU3nf "
"yKU6ngz sdJ4W5O pjVcyoy ZNuPWqZ O0OSVFt "
"J160xpm 2j1IAyf b4xtltc E9MflTP NDioDZg TCmLjeT "
"rYxQaTa MvN7kTU Uni02EK cG5UYCf GC8V8CQ 7o1qq10").split()
loc = """PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"#
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"#
VALE_TENEBROSO = "https://i.imgur.com/OZE1myn.jpg"#
PORTAO_OURO = "https://i.imgur.com/J6ow4jR.jpg"#
PORTAO_PRATA = "https://i.imgur.com/v0g7eGm.jpg"#
PORTAO_COBRE = "https://i.imgur.com/45aU3nf.jpg"#
PORTAO_FERRO = "https://i.imgur.com/yKU6ngz.jpg"#
ATALAIA = "https://i.imgur.com/sdJ4W5O.jpg"#
JARDIM_SUSSUROS = "https://i.imgur.com/pjVcyoy.jpg"#
PISTA_POUSO = "https://i.imgur.com/CU3TLYh.png"#
JARDIM_UIVOS = "https://i.imgur.com/ZNuPWqZ.jpg"#
TEMPLO_SOL = "https://i.imgur.com/O0OSVFt.jpg"#
TEMPLO_LUA = "https://i.imgur.com/J160xpm.jpg"#
CAVERNA_LAVA = "https://i.imgur.com/2j1IAyf.jpg"#
CAVERNA_SOMBRAS = "https://i.imgur.com/b4xtltc.png"#
OBSERVATORIO = "https://i.imgur.com/E9MflTP.jpg"#
PANTANO_BRUMAS = "https://i.imgur.com/NDioDZg.jpg"#
ROCHA_FANTASMA = "https://i.imgur.com/TCmLjeT.png"#
PALACIO_MARES = "https://i.imgur.com/rYxQaTa.png"#
PENHASCO_ABANDONO = "https://i.imgur.com/MvN7kTU.jpg"#
BOSQUE_CARMESIM = "https://i.imgur.com/Uni02EK.jpg"#
DUNAS_ENGANO = "https://i.imgur.com/cG5UYCf.jpg"#
PONTE_SUSPENSA = "https://i.imgur.com/GC8V8CQ.jpg"#
LAGOA_PERDIDA = "https://i.imgur.com/7o1qq10.png"#"""
PAWN = "https://imgur.com/zO3kiRp.png"
Cah = namedtuple("Cah", "nome link elemento")

class IlhaProibida:
    """ Representa a classe principal do Jogo.
    
    Terrenos 
        Locais onde os peões podem ficar.
        
    """

    def __init__(self):
        self.oceano = Cena(IMAGEM).vai()
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        #self.peao = Peao(self)
        #self.peao.mover(self.terrenos[0])

    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        from random import shuffle, sample
        """info_terrenos = it = [
        PORTAO_OURO, PALACIO_CORAL, PORTAO_BRONZE, VALE_TENEBROSO, CAVERNA_LAVA, PORTAO_FERRO,
        CAVERNA_SOMBRAS, OBSERVATORIO, PANTANO_BRUMAS, ROCHA_FANTASMA, PALACIO_MARES, JARDIM_SUSSUROS,
        PENHASCO_ABANDONO, BOSQUE_CARMESIM, DUNAS_ENGANO, PONTE_SUSPENSA, PORTAO_PRATA,
        PORTAO_COBRE, ATALAIA, PISTA_POUSO, JARDIM_UIVOS, TEMPLO_SOL, TEMPLO_LUA, LAGOA_PERDIDA]"""
        it = LINKS[:]
        nm = NOMES[:]
        locais = [Cah(nome=nm.pop(), link=it.pop(), elemento=None) for _ in range(len(it))]
        spl = sample(list(range(1,24)), 8)
        tfavs = zip(spl,TFAVS *2)
        for loc, elt_ in tfavs:
            #lc, ln, tf_ = locais[loc].nome
            locais[loc] = Cah(nome=locais[loc].nome, link=locais[loc].link, elemento=elt_)
        [self.terrenos[loc].elemento(tfav) for loc, tfav in tfavs]
        shuffle(locais)
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=locais.pop(), ilha=self)
                         for px in range(36) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
                                 #posx=((px % 6) + int(abs(2.5 - px // 6))), local=lc, ilha=self)
                         #for px, lc in enumerate(info_terrenos[:36]) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        #self.terrenos[4].afundar()


class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, local, posx, posy, cena, ilha):
        FOLGA = LADO + 10
        link = f"https://i.imgur.com/{local.link}.jpg"
        self.local = Elemento(link, x=posx * FOLGA + 10, y=posy * FOLGA + 30, w=LADO, h=LADO,
                              cena=cena)
        style = {'background-color': '#222', 'font-size': '10px', 'text-align': 'center', 'color': '#FFF'}
        tit = Elemento('', w=LADO, h=LADO//6, cena=self.local, style=style)
        tit.elt.text = local.nome.replace('_',' ') #"UM LOCAL QUALQUER"
        self.peao, self.ilha = None, ilha
        self.posx, self.posy = posx, posy
        #self.local.vai = self.vai
        self.elemento(local.elemento)
        self.afunda = False
        
    def elemento(self, tipo):
        if not tipo:
            return
        style = {'bottom': '0px', 'left': '0px'}
        elemt = Elemento(f"https://i.imgur.com/{tipo}.png", y=LADO//5, x=-5, w=LADO//2, h=4*LADO//5+5, cena=self.local, style=style)
        #tit.elt.text = local.nome.replace('_',' ') #"UM LOCAL QUALQUER"
    

def util():
    # ln = " ".join([ln for ln in loc.split("\n") if ln]) # for t in ln if t])
    ln = " ".join([ln.split()[0] for ln in loc.split("\n") if ln])
    print(ln)
    ln = " ".join([ln.split()[-1].split("/")[-1][:-6] for ln in loc.split("\n") if ln])
    print(ln)
    
if __name__ == "__main__":
    IlhaProibida()
