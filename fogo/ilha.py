# radia.fogo.ilha.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""Página Montagem do Tabulheiro (Ilha) do jogo Ilha Proibida Equipe Fogo.

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor::  Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>

Changelog
---------
.. versionadded::    23.11
        Descreva o que você adicionou no código.

"""
import random

NOMES = ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
"PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
"TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
"PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()

class IlhaProibida:
    """
    classe ilha proibida
    """
    def __init__(self, jogadores=None):
        if jogadores is None:
            jogadores = []
        baralho_tesouro = bt = list("tafv" * 5 +"dd" + "hhh")
        baralho_alaga = ba = "eee" 
        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in bt]
        # recursos do jogador para relizar capturas, drenagem e movimentos
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
        # acrescido de um conjunto de cartas que causam uma enchente
        self.cartas_inunda = list(range(24))
        # abaixa um terreno que fica alagado ou afunda no oceano
        print("Bemvindos à Ilha Poibida - montagem do tabuleiro")
        self.terrenos = []
        self.monta_tabuleiro_oceano(jogadores)

    def monta_tabuleiro_oceano(self, jogadores):
        """ Montar o tabuleiro em forma de diamante.

        """
        from random import shuffle
        tafv = [" "] * 15 + list("tafv") * 2
        shuffle(tafv)

        # o primeiro é o helicoptero, deve ser sem tafv
        tafv = [" "] + tafv
        self.terrenos = [Terreno(nome=NOMES.pop(0), tafv=tafv.pop(0)) for _ in range(24)]
        shuffle(self.terrenos)

        for jogador in jogadores:
            self.terrenos[random.randrange(0, len(self.terrenos))].coloquar_jogador(jogador)

        spaces = 21

        tabuleiro = "|" + " " * spaces + "|" + " " * spaces + "| "
        for ter in self.terrenos[:2]:
            tabuleiro += ter.string_rep() + " | "
        tabuleiro += " " * (spaces - 1) + "|" + " " * spaces + "| "
        print(tabuleiro)

        tabuleiro = "|" + " " * spaces + "| "
        for ter in self.terrenos[2:6]:
            tabuleiro += ter.string_rep() + " | "
        tabuleiro += " " * (spaces - 1) + "| "
        print(tabuleiro)

        tabuleiro = "| "
        for ter in self.terrenos[6:12]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)

        tabuleiro = "| "
        for ter in self.terrenos[12:18]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)

        tabuleiro = "|" + " " * spaces + "| "
        for ter in self.terrenos[18:22]:
            tabuleiro += ter.string_rep() + " | "
        tabuleiro += " " * (spaces - 1) + "|" + " " * spaces + "| "
        print(tabuleiro)

        tabuleiro = "|" + " " * spaces + "|" + " " * spaces + "| "
        for ter in self.terrenos[22:]:
            tabuleiro += ter.string_rep() + " | "
        tabuleiro += " " * (spaces - 1) + "|" + " " * spaces + "| "
        print(tabuleiro)

        # Cada terreno realmente criado "puxa" um terreno da lista de "Ter's
        # self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
        #                          posx=((px % 6) + int(abs(2.5 - px // 6))), local=it.pop(0), ilha=self)
        #                  for px in range(36) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]



class CartaTesouro:
    def __init__(self, face):
        self.face = face


class CartaAlagamento(CartaTesouro):
    def __init__(self, face):
        super().__init__(face)


class Terreno:
    def __init__(self, nome, tafv):
        self.nome = nome
        self.tafv = tafv
        self.jogadores = []

    def string_rep(self):
        result = self.nome + " " + self.tafv
        if len(self.jogadores) > 0:
            result += " " + ''.join([jog.nome[0] for jog in self.jogadores])
        else:
            result += " -"

        faltam = 19 - len(result)
        return result + " " * faltam

    def coloquar_jogador(self, jogador):
        self.jogadores.append(jogador)
        
        
if __name__ == "__main__":
    IlhaProibida()