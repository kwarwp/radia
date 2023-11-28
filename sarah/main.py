# radia.sarah.main.py
# __author__ Filipe Marçal
import random
class Carta:
    class Alagamento:
        class PORTAO_COBRE:
            nome = "Portão de Cobre"
            contagem = 0
        class PISTA_POUSO:
            nome = "Pista de Pouso"
            contagem = 0
        class PORTAO_BRONZE:
            nome = "Portão de Bronze"
            contagem = 0
        class PALACIO_CORAL:
            nome = "Palácio de Coral"
            contagem = 0
        class VALE_TENEBROSO:
            nome = "Vale Tenebroso"
            contagem = 0
        class PORTAO_OURO:
            nome = "Portão de Ouro"
            contagem = 0
        class PORTAO_PRATA:
            nome = "Portão de Prata"
            contagem = 0
        class PORTAO_FERRO:
            nome = "Portão de Ferro"
            contagem = 0
        class ATALAIA:
            nome = "Atalaia"
            contagem = 0
        class JARDIM_SUSSUROS:
            nome = "Jardim dos Sussurros"
            contagem = 0
        class JARDIM_UIVOS:
            nome = "Jardim dos Uivos"
            contagem = 0
        class TEMPLO_SOL:
            nome = "Templo do Sol"
            contagem = 0
        class TEMPLO_LUA:
            nome = "Templo da Lua"
            contagem = 0
        class CAVERNA_LAVA:
            nome = "Caverna de Lava"
            contagem = 0
        class CAVERNA_SOMBRAS:
            nome = "Caverna das Sombras"
            contagem = 0
        class OBSERVATORIO:
            nome = "Observatório"
            contagem = 0
        class PANTANO_BRUMAS:
            nome = "Pântano de Brumas"
            contagem = 0
        class ROCHA_FANTASMA:
            nome = "Rocha Fantasma"
            contagem = 0
        class PALACIO_MARES:
            nome = "Palácio dos Mares"
            contagem = 0
        class PENEDO_BALDIO:
            nome = "Penedo Baldio"
            contagem = 0
        class BOSQUE_CARMESIM:
            nome = "Bosque Carmesim"
            contagem = 0
        class DUNAS_ENGANO:
            nome = "Dunas do Engano"
            contagem = 0
        class PONTE_SUSPENSA:
            nome = "Ponte Suspensa"
            contagem = 0
        class LAGOA_PERDIDA:
            nome = "Lagoa Perdida"
            contagem = 0

    class Tesouro:
        class Terra:
            nome = "A Pedra da Terra"
            contagem = 0
        class Vento:
            nome = "A Estátua de Vento"
            contagem = 0
        class Fogo:
            nome = "O Cristal de Fogo"
            contagem = 0
        class Agua:
            nome = "O Cálice de Oceano"
            contagem=0

    class Aventureiro:
        class Explorador:
            nome = "Explorador"
            contagem = 0

        class Piloto:
            nome = "Piloto"
            contagem = 0

        class Engenheiro:
            nome = "Engenheiro"
            contagem = 0

        class Mergulhador:
            nome = "Mergulhador"
            contagem = 0

        class Navegador:
            nome = "Navegador"
            contagem = 0
class Terreno:
    class PORTAO_COBRE:
        nome = "Portão de Cobre"
        visual = '\u2fa8C'
        contagem = 0
    class PISTA_POUSO:
        nome = "Pista de Pouso"
        visual = '\U0001f681 '
        contagem = 0

    class PORTAO_BRONZE:
        nome = "Portão de Bronze"
        visual = '\u2fa8 B'
        contagem = 0
    class PALACIO_CORAL:
        nome = "Palácio de Coral"
        visual = ' '
        contagem = 0

    class VALE_TENEBROSO:
        nome = "Vale Tenebroso"
        visual = ' \U0001f47b'
        contagem = 0

    class PORTAO_OURO:
        nome = "Portão de Ouro"
        visual = '\u2fa8 O'
        contagem = 0

    class PORTAO_PRATA:
        nome = "Portão de Prata"
        visual = '\u2fa8 P'
        contagem = 0

    class PORTAO_FERRO:
        nome = "Portão de Ferro"
        visual = '\u2fa8 F'
        contagem = 0

    class ATALAIA:
        nome = "Atalaia"
        visual = '\u265c '
        contagem = 0

    class JARDIM_SUSSUROS:
        nome = "Jardim dos Sussurros"
        visual = '\u2698 '
        contagem = 0

    class JARDIM_UIVOS:
        nome = "Jardim dos Uivos"
        visual = '\u2698 \U0001f43a'
        contagem = 0

    class TEMPLO_SOL:
        nome = "Templo do Sol"
        visual = "\uf90a \u263c"
        contagem = 0

    class TEMPLO_LUA:
        nome = "Templo da Lua"
        visual = "\uf90a \u263e"
        contagem = 0

    class CAVERNA_LAVA:
        nome = "Caverna de Lava"
        visual = ''
        contagem = 0

    class CAVERNA_SOMBRAS:
        nome = "Caverna das Sombras"
        visual = "Λ *"
        contagem = 0

    class OBSERVATORIO:
        nome = "Observatório"
        visual = "\u265c"
        contagem = 0

    class PANTANO_BRUMAS:
        nome = "Pântano de Brumas"
        visual = "  \u2601"
        contagem = 0

    class ROCHA_FANTASMA:
        nome = "Rocha Fantasma"
        visual = " "
        contagem = 0

    class PALACIO_MARES:
        nome = "Palácio dos Mares"
        visual = ""
        contagem = 0

    class PENEDO_BALDIO:
        nome = "Penedo Baldio"
        visual = "ㄱ "
        contagem = 0

    class BOSQUE_CARMESIM:
        nome = "Bosque Carmesim"
        visual = " ❤"
        contagem = 0

    class DUNAS_ENGANO:
        nome = "Dunas do Engano"
        visual = "⏳"
        contagem = 0

    class PONTE_SUSPENSA:
        nome = "Ponte Suspensa"
        visual = " "
        contagem = 0

    class LAGOA_PERDIDA:
        nome = "Lagoa Perdida"
        visual = " "
        contagem = 0
class Ilha:
    Ter = [Terreno.PISTA_POUSO.visual, Terreno.PORTAO_COBRE.visual, Terreno.PORTAO_BRONZE.visual, Terreno.PALACIO_CORAL.visual, Terreno.VALE_TENEBROSO.visual, Terreno.PORTAO_OURO.visual, Terreno.PORTAO_PRATA.visual, Terreno.PORTAO_FERRO.visual, Terreno.ATALAIA.visual, Terreno.JARDIM_SUSSUROS.visual, Terreno.JARDIM_UIVOS.visual, Terreno.TEMPLO_SOL.visual, Terreno.TEMPLO_LUA.visual, Terreno.CAVERNA_LAVA.visual, Terreno.CAVERNA_SOMBRAS.visual, Terreno.OBSERVATORIO.visual, Terreno.PANTANO_BRUMAS.visual, Terreno.ROCHA_FANTASMA.visual, Terreno.PALACIO_MARES.visual, Terreno.PENEDO_BALDIO.visual, Terreno.BOSQUE_CARMESIM.visual,Terreno.DUNAS_ENGANO.visual,Terreno.PONTE_SUSPENSA.visual,Terreno.LAGOA_PERDIDA.visual]
    matriz = [["" for i in range(6)]for j in range(6)]
    #Adicionando elementos
    matriz[0][0] = "    "
    matriz[0][1] = "    "
    elemento = random.choice(Ter)
    matriz[0][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[0][3] = elemento
    Ter.remove(elemento)
    matriz[0][4] = "    "
    matriz[0][5] = "    "
    matriz[1][0] = "    "
    elemento = random.choice(Ter)
    matriz[1][1] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[1][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[1][3] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[1][4] = elemento
    Ter.remove(elemento)
    matriz[1][5]="  "
    elemento = random.choice(Ter)
    matriz[2][0] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[2][1] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[2][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[2][3] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[2][4] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[2][5] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][0] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][1] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][3] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][4] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[3][5] = elemento
    Ter.remove(elemento)
    matriz[4][0] = "    "
    elemento = random.choice(Ter)
    matriz[4][1] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[4][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[4][3] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[4][4] = elemento
    Ter.remove(elemento)
    matriz[4][5] = "  "
    matriz[5][0] = "    "
    matriz[5][1] = "    "
    elemento = random.choice(Ter)
    matriz[5][2] = elemento
    Ter.remove(elemento)
    elemento = random.choice(Ter)
    matriz[5][3] = elemento
    Ter.remove(elemento)
    matriz[5][4]="  "
    matriz[5][5]="  "
class Descarte:
    class Tesouro:
        pass
    class Alagamento:
        pass
class Cartas:
    Baralho = [Carta.Tesouro.Terra.nome, Carta.Tesouro.Agua.nome, Carta.Tesouro.Fogo.nome , Carta.Tesouro.Vento.nome, Carta.Aventureiro.Piloto.nome,Carta.Aventureiro.Navegador.nome, Carta.Aventureiro.Engenheiro.nome, Carta.Aventureiro.Explorador.nome, Carta.Aventureiro.Mergulhador.nome]
#Inserir na primeira linha, coluna 3
#Remover o valor escolhido da lista Ilha.listaTerrenos
    for i in range(6):
        print(Ilha.matriz[i])