# radia.agua.ilha.py
# SPDX-License-Identifier: GPL-3.0-or-later
# radia.agua.main.py
"""A Ilha é o módulo de estruturação e início do jogo.

LOG - http://bit.ly/Dev_Agile_23

EQUIPE Água

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
    Divisão de equipes (07).
    
.. versionadded::    23.10
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""


class IlhaProibida:
    def __init__(self):
        baralho_tesouro = bt = list("tafv" * 5 +"dd" + "hhh")
        baralho_alaga = ba = list("eee")
        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in bt]
        # recursos do jogador para relizar capturas, drenagem e movimentos
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
        # acrescido de um conjunto de cartas que causam uma enchente
        self.cartas_inunda = list(range(24))
        # abaixa um terreno que fica alagado ou afunda no oceano
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        print("cartas tesouro:" self.cartas_tesouro)
        print("cartas de inundacao:" self.cartas_inunda)
        
    def distribuir_cartas_tesouro(self)


class CartaTesouro:
    def __init__(self, face):
        self.face = face
        #print("Bemvindos à Ilha Poibida - montagem do tabuleiro")


class CartaAlagamento(CartaTesouro):
    def __init__(self, face):
        super().__init__(self, face)
        #print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
            
        
        
if __name__ == "__main__":
    IlhaProibida()