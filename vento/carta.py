# radia.vento.carta.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    23.12
        Descreva o que você adicionou no código.

"""
class Carta:
    pass

class CartaAlagamento(Carta):
    def __init__(self, nome):
        self.nome = nome

class CartaTesouro(Carta):
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class CartaEnchente(Carta):
    def __repr__(self):
        return "   CARTA ENCHENTE   "

class CartaHelicoptero(Carta):
    def __repr__(self):
        return " CARTA HELICOPTERO "

class CartaSacoAreia(Carta):
    def __repr__(self):
        return "CARTA SACO DE AREIA"
