# radia.fogo.test_unnitest.py
# __author__ Fernanda, Finn, Anderson, Vanessa
"""Página de teste do módulo ilha.py do jogo Ilha Proibida da Equipe Fogo.

EQUIPE FOGO

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor::  Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>

Changelog
---------
.. versionadded::    10.12
   test 1

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

import unittest

import ilha

class TestTerrenos(unittest.TestCase):
    def test_jogadores(self):
        '''
        Define um Teste unitario para a funcao monta_tabuleiro_oceano do modulo fogo.ilha
        usando a biblioteca unnittest. Verifica o numero_cartas em self.terrenos.
        '''
        self.assert len(self.terrenos) == 24, "O número de terrenos deve ser 24"

        def test_2(self):
        '''
        test2
        '''
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()