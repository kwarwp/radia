# radia.fogo.main.py
# __author__ Fernanda, Finn, Vanessa
"""Página de entrada do jogo Ilha Proibida.

LOG - http://bit.ly/Dev_Agile_23

EQUIPE FOGO 

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor::  Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>


Changelog
---------
.. versionadded::    23.11
    classe jogador e MaoJogador (07).


|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

class Jogador:
    def __init__(self, nome="DefaultPlayer"):
        self.nome = nome
        self.mao = MaoJogador(dono=self)
        print(f"{self.nome} se apresentando")


class MaoJogador:
    def __init__(self, dono, cartas=[]):
        self.dono = dono
        self.cartas = cartas
        print(f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")
        
        
if __name__ == "__main__":
    #IlhaProibida()
    Jogador()
    