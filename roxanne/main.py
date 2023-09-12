# radia.roxanne.main.py
# __author__ Carlo
from _spy.vitollino.main import Cena, Elemento
IMAGEM = 'https://www.comciencia.br/wp-content/uploads/2021/09/oceano2-672x372.jpg'
PORTAO_BRONZE= "https://img.freepik.com/fotos-premium/fragmento-de-portao-de-bronze-de-ferro-forjado_172420-936.jpg?w=2000"
oceano = Cena(IMAGEM).vai()
portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)

