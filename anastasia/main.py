# radia.anastasia.main.py
#_author_vanessa
print("alo")#escrito
from _spy.vitollino.main import Cena, Elemento #Cena C maiusculo porque é classe  Elemento peçinhas que colocam na cena 
IMAGEM = "https://www.mafiadomergulho.com.br/wp-content/uploads/2021/04/fundo-do-mar-site-copy.jpg" #COLOCAR IMAGEM DA INTERNET 
PORTAO_BRONZE = "https://imgur.com/bl61b7H.jpg"


class IlhaProibida:  # : significa inicio de um bloco então posteriormente tem que estar intendado
    def __init__(self): #construcao, o primeiro parametro sempre se chama self
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        
IlhaProibida()