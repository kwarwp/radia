# radia.sara.main.py
# Fernanda - POO 2023 - UFRJ
from _spy.vitollino.main import Cena, Elemento
IMAGEM = 'https://dinamicambiental.com.br/wp-content/uploads/2021/06/o-oceano-e-a-nossa-sobrevivencia.jpg'
PORTAO_BRONZE = 'https://thumbs.dreamstime.com/z/batedor-de-bronze-em-forma-uma-cabe%C3%A7a-le%C3%A3o-do-port%C3%A3o-da-catedral-col%C3%B4nia-na-alemanha-194660830.jpg?w=992'
#Cena(IMAGEM).vai()
oceano = Cena(IMAGEM).vai()
portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano) 

