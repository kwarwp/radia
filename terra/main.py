# radia.agua.main.py
"""Página de entrada do jogo Ilha Proibida.

LOG - https://bit.ly/Dev_Agile_23

EQUIPE Terra 
.. codeauthor:: Keila Lima de Oliveira <keila90.if@gmail.com>
.. codeauthor:: Felipe Nunes <felipenunes.7921@gmail.com>
.. codeauthor:: Leonardo Cesar <leonardocesarc@gmail.com>
.. codeauthor:: Pedro França <pedro.franca@ufrj.br>

Changelog
---------
.. versionadded::    23.11
    Divisão de equipes (07).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from terra import LG


class IlhaProibida:
    def __init__(self):
        LG.log(0, "Bem vindos à Ilha Proibida da Equipe Terra  !")


def main():
    IlhaProibida()


if __name__ == "__main__":
    main()
