
import unittest
from fogo.ilha import IlhaProibida as
from fogo.jogador import Jogador

class TestIlhaProibida(unittest.TestCase):

    def test_numero_jogadores(self):
        # Crie uma instância de IlhaProibida com uma lista de jogadores
        jogadores = ['Jogador1', 'Jogador2', 'Jogador3']
        jogo = IlhaProibida(Jogador)

        # Verifique se o número de jogadores na instância do jogo é igual ao número de jogadores fornecidos
        self.assertEqual(len(jogo.Jogador), len(Jogador))

if __name__ == '__main__':
    unittest.main()