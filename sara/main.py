# radia.sara.main.py
# Fernanda - POO 2023 - UFRJ
from _spy.vitollino.main import Cena, Elemento
IMAGEM = 'https://dinamicambiental.com.br/wp-content/uploads/2021/06/o-oceano-e-a-nossa-sobrevivencia.jpg'
PORTAO_BRONZE = 'https://thumbs.dreamstime.com/z/batedor-de-bronze-em-forma-uma-cabe%C3%A7a-le%C3%A3o-do-port%C3%A3o-da-catedral-col%C3%B4nia-na-alemanha-194660830.jpg?w=992'
PALACIO_CORAL = 'https://img.freepik.com/fotos-premium/palacio-subaquatico-com-ilustracao-colorida-de-ia-generativa-de-corais-e-peixes_268722-1554.jpg?w=740'
#Cena é classe e cena é atributo

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        portao = Elemento(PALACIO_CORAL, x=110, y=10, w=100, h=100, cena=oceano)
        


IlhaProibida()