# radia.vento.cartas.py
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
        from random import shuffle
        baralho_tesouro = bt = list("tafv" * 5 +"dd" + "hhh")
        baralho_alaga = ba = list("eee")
        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in bt]
        # recursos do jogador para relizar capturas, drenagem e movimentos
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
        # acrescido de um conjunto de cartas que causam uma enchente
        self.cartas_inunda = list(range(24))
        shuffle(self.cartas_inunda)
        shuffle(self.cartas_tesouro)
        # abaixa um terreno que fica alagado ou afunda no oceano
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        print("cartas tesouro:", self.cartas_tesouro)
        print("cartas de inundacao:", self.cartas_inunda)
        print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
        
    def distribuir_cartas_tesouro(self,cartas):
        return random.sample(cartas,2)


class CartaTesouro:
    def __init__(self, face):
        self.face = face
        #print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        
    def __repr__(self):
        return self.face


class CartaAlagamento(CartaTesouro):
    def __init__(self, face):
        super().__init__(face)
        #print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        
    def __repr__(self):
        return ""  # self.face 
            
        
        
if __name__ == "__main__":
    IlhaProibida()