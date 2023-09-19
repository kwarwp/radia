# radia.naomi.main.py
# __author__Felipe

from _spy.vitollino.main import Cena, Elemento,STYLE
ILHA = "https://imguh.com/images/2023/09/19/fnunes._picture_this_a_big_ocean_image_with_a_big_island_full_o_2c948b96-ce3e-466e-bab1-5a6c30e7c7e3-1d81919711bc32953.png"
PORTAO_BRONZE = ""
STYLE["width"] = 800 
STYLE["height"] = "600px"

class ilhaProibida:
    def __init__(self):
        tabuleiro = Cena(ILHA).vai().center()
        #portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        
ilhaProibida()