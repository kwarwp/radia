# teste_jogador.py

import unittest
import fogo.ilha import IlhaProibida

class TesteCartasTabuleiro(unittest.TestCase):

    def test_contacartas(self, terrenos):
        # importar de cartas de tabuleiro de IlhaProibida em uma lista

        self.assertEqual(24, terrenos)  # add assertion here

if __name__ == '__main__':
    unittest.main()
