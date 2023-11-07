# radia.fogo.ilha.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    23.11
        Descreva o que você adicionou no código.

"""

class IlhaProibida:
    def __init__(self):
        baralho_tesouro = bt = list("tafv" * 5 +"dd" + "hhh")
        baralho_alaga = ba = "eee" 
        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in bt]
        # recursos do jogador para relizar capturas, drenagem e movimentos
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
        # acrescido de um conjunto de cartas que causam uma enchente
        self.cartas_inunda = list(range(24))
        # abaixa um terreno que fica alagado ou afunda no oceano
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")


class CartaTesouro:
    def __init__(self, face):
        self.face = face


class CartaAlagamento(CartaTesouro):
    def __init__(self, face):
        super(self, face)
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        
        
        
        
if __name__ == "__main__":
    IlhaProibida()