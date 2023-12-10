#pytest in action - test_ilha.py
'''
Este script define um teste unitario para a função xxxx usando a biblioteca pytest.
Por meio do comando pytest test_pytest.py no terminal é executado o teste.
'''

import pytest
from fogo.ilha import monta_tabuleiro_oceano

def test_monta_tabuleiro_oceano():
    '''
    Teste unitario na funcao monta_tabuleiro_oceano
    verificar número de cartas = 24
    '''
        numero_cartas = len(terrenos)
        assert numero_cartas == 24, f"O número de cartas sorteadas é {numero_cartas}, não 24."

verificar_numero_cartas(self.terrenos)