# radia.fogo.main.py
# radia.roxanne.main.py
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
    Divisão de equipes (07).
    
.. versionadded::    23.10
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""


from fogo.ilha import IlhaProibida as Ilha 
from fogo.jogador import Jogador 


class IlhaProibida:
    def __init__(self):
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        
        
if __name__ == "__main__":
    IlhaProibida()