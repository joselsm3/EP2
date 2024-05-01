import random
from time import sleep
from constantes import CONFIGURACAO, PAISES, ALFABETO, DICIONARIO_CORES
lista_denumeros2=['1','2','3','4','5','6','7','8','9','10']
numletra={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}
lista_denumeros=['1','2','3','4','5']
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
def printa_string_bombardeio(l1,l2,lista):
    for i in range(len(lista)): 
        for l in range(len(lista[i])): 
            if l1[i][l] == "X": 
                cor = "X"
                l1[i][l] = DICIONARIO_CORES[cor]
            elif l1[i][l] == "A": 
                cor = "A"
                l1[i][l] = DICIONARIO_CORES[cor]
    for i in range(len(l2)): 
        for l in range(len(l2[i])): 
            if l2[i][l] == "A": 
                cor = "A"
                l2[i][l] = DICIONARIO_CORES[cor]
            elif l2[i][l] == "X": 
                cor = "X"
                l2[i][l] = DICIONARIO_CORES[cor]
    print(f"        COMPUTADOR -                                                        JOGADOR -")
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    print(f'  1{l1[0][0]}{l1[0][1]}{l1[0][2]}{l1[0][3]}{l1[0][4]}{l1[0][5]}{l1[0][6]}{l1[0][7]}{l1[0][8]}{l1[0][9]}1                             1{l2[0][0]}{l2[0][1]}{l2[0][2]}{l2[0][3]}{l2[0][4]}{l2[0][5]}{l2[0][6]}{l2[0][7]}{l2[0][8]}{l2[0][9]}1')
    print(f'  2{l1[1][0]}{l1[1][1]}{l1[1][2]}{l1[1][3]}{l1[1][4]}{l1[1][5]}{l1[1][6]}{l1[1][7]}{l1[1][8]}{l1[1][9]}2                             2{l2[1][0]}{l2[1][1]}{l2[1][2]}{l2[1][3]}{l2[1][4]}{l2[1][5]}{l2[1][6]}{l2[1][7]}{l2[1][8]}{l2[1][9]}2')
    print(f'  3{l1[2][0]}{l1[2][1]}{l1[2][2]}{l1[2][3]}{l1[2][4]}{l1[2][5]}{l1[2][6]}{l1[2][7]}{l1[2][8]}{l1[2][9]}3                             3{l2[2][0]}{l2[2][1]}{l2[2][2]}{l2[2][3]}{l2[2][4]}{l2[2][5]}{l2[2][6]}{l2[2][7]}{l2[2][8]}{l2[2][9]}3')
    print(f'  4{l1[3][0]}{l1[3][1]}{l1[3][2]}{l1[3][3]}{l1[3][4]}{l1[3][5]}{l1[3][6]}{l1[3][7]}{l1[3][8]}{l1[3][9]}4                             4{l2[3][0]}{l2[3][1]}{l2[3][2]}{l2[3][3]}{l2[3][4]}{l2[3][5]}{l2[3][6]}{l2[3][7]}{l2[3][8]}{l2[3][9]}4')
    print(f'  5{l1[4][0]}{l1[4][1]}{l1[4][2]}{l1[4][3]}{l1[4][4]}{l1[4][5]}{l1[4][6]}{l1[4][7]}{l1[4][8]}{l1[4][9]}5                             5{l2[4][0]}{l2[4][1]}{l2[4][2]}{l2[4][3]}{l2[4][4]}{l2[4][5]}{l2[4][6]}{l2[4][7]}{l2[4][8]}{l2[4][9]}5')
    print(f'  6{l1[5][0]}{l1[5][1]}{l1[5][2]}{l1[5][3]}{l1[5][4]}{l1[5][5]}{l1[5][6]}{l1[5][7]}{l1[5][8]}{l1[5][9]}6                             6{l2[5][0]}{l2[5][1]}{l2[5][2]}{l2[5][3]}{l2[5][4]}{l2[5][5]}{l2[5][6]}{l2[5][7]}{l2[5][8]}{l2[5][9]}6')
    print(f'  7{l1[6][0]}{l1[6][1]}{l1[6][2]}{l1[6][3]}{l1[6][4]}{l1[6][5]}{l1[6][6]}{l1[6][7]}{l1[6][8]}{l1[6][9]}7                             7{l2[6][0]}{l2[6][1]}{l2[6][2]}{l2[6][3]}{l2[6][4]}{l2[6][5]}{l2[6][6]}{l2[6][7]}{l2[6][8]}{l2[6][9]}7')
    print(f'  8{l1[7][0]}{l1[7][1]}{l1[7][2]}{l1[7][3]}{l1[7][4]}{l1[7][5]}{l1[7][6]}{l1[7][7]}{l1[7][8]}{l1[7][9]}8                             8{l2[7][0]}{l2[7][1]}{l2[7][2]}{l2[7][3]}{l2[7][4]}{l2[7][5]}{l2[7][6]}{l2[7][7]}{l2[7][8]}{l2[7][9]}8')
    print(f'  9{l1[8][0]}{l1[8][1]}{l1[8][2]}{l1[8][3]}{l1[8][4]}{l1[8][5]}{l1[8][6]}{l1[8][7]}{l1[8][8]}{l1[8][9]}9                             9{l2[8][0]}{l2[8][1]}{l2[8][2]}{l2[8][3]}{l2[8][4]}{l2[8][5]}{l2[8][6]}{l2[8][7]}{l2[8][8]}{l2[8][9]}9')
    print(f' 10{l1[9][0]}{l1[9][1]}{l1[9][2]}{l1[9][3]}{l1[9][4]}{l1[9][5]}{l1[9][6]}{l1[9][7]}{l1[9][8]}{l1[9][9]}10                           10{l2[9][0]}{l2[9][1]}{l2[9][2]}{l2[9][3]}{l2[9][4]}{l2[9][5]}{l2[9][6]}{l2[9][7]}{l2[9][8]}{l2[9][9]}10')            
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    return ""
def printa_string(l1,l2):
    for i in range(len(l2)): 
        for l in range(len(l2[i])): 
            if l2[i][l] == "N": 
                cor = "V"
                l2[i][l] = DICIONARIO_CORES[cor]
    print("        COMPUTADOR                                                       JOGADOR") 
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    print(f'  1{l1[0][0]}{l1[0][1]}{l1[0][2]}{l1[0][3]}{l1[0][4]}{l1[0][5]}{l1[0][6]}{l1[0][7]}{l1[0][8]}{l1[0][9]}1                             1{l2[0][0]}{l2[0][1]}{l2[0][2]}{l2[0][3]}{l2[0][4]}{l2[0][5]}{l2[0][6]}{l2[0][7]}{l2[0][8]}{l2[0][9]}1')
    print(f'  2{l1[1][0]}{l1[1][1]}{l1[1][2]}{l1[1][3]}{l1[1][4]}{l1[1][5]}{l1[1][6]}{l1[1][7]}{l1[1][8]}{l1[1][9]}2                             2{l2[1][0]}{l2[1][1]}{l2[1][2]}{l2[1][3]}{l2[1][4]}{l2[1][5]}{l2[1][6]}{l2[1][7]}{l2[1][8]}{l2[1][9]}2')
    print(f'  3{l1[2][0]}{l1[2][1]}{l1[2][2]}{l1[2][3]}{l1[2][4]}{l1[2][5]}{l1[2][6]}{l1[2][7]}{l1[2][8]}{l1[2][9]}3                             3{l2[2][0]}{l2[2][1]}{l2[2][2]}{l2[2][3]}{l2[2][4]}{l2[2][5]}{l2[2][6]}{l2[2][7]}{l2[2][8]}{l2[2][9]}3')
    print(f'  4{l1[3][0]}{l1[3][1]}{l1[3][2]}{l1[3][3]}{l1[3][4]}{l1[3][5]}{l1[3][6]}{l1[3][7]}{l1[3][8]}{l1[3][9]}4                             4{l2[3][0]}{l2[3][1]}{l2[3][2]}{l2[3][3]}{l2[3][4]}{l2[3][5]}{l2[3][6]}{l2[3][7]}{l2[3][8]}{l2[3][9]}4')
    print(f'  5{l1[4][0]}{l1[4][1]}{l1[4][2]}{l1[4][3]}{l1[4][4]}{l1[4][5]}{l1[4][6]}{l1[4][7]}{l1[4][8]}{l1[4][9]}5                             5{l2[4][0]}{l2[4][1]}{l2[4][2]}{l2[4][3]}{l2[4][4]}{l2[4][5]}{l2[4][6]}{l2[4][7]}{l2[4][8]}{l2[4][9]}5')
    print(f'  6{l1[5][0]}{l1[5][1]}{l1[5][2]}{l1[5][3]}{l1[5][4]}{l1[5][5]}{l1[5][6]}{l1[5][7]}{l1[5][8]}{l1[5][9]}6                             6{l2[5][0]}{l2[5][1]}{l2[5][2]}{l2[5][3]}{l2[5][4]}{l2[5][5]}{l2[5][6]}{l2[5][7]}{l2[5][8]}{l2[5][9]}6')
    print(f'  7{l1[6][0]}{l1[6][1]}{l1[6][2]}{l1[6][3]}{l1[6][4]}{l1[6][5]}{l1[6][6]}{l1[6][7]}{l1[6][8]}{l1[6][9]}7                             7{l2[6][0]}{l2[6][1]}{l2[6][2]}{l2[6][3]}{l2[6][4]}{l2[6][5]}{l2[6][6]}{l2[6][7]}{l2[6][8]}{l2[6][9]}7')
    print(f'  8{l1[7][0]}{l1[7][1]}{l1[7][2]}{l1[7][3]}{l1[7][4]}{l1[7][5]}{l1[7][6]}{l1[7][7]}{l1[7][8]}{l1[7][9]}8                             8{l2[7][0]}{l2[7][1]}{l2[7][2]}{l2[7][3]}{l2[7][4]}{l2[7][5]}{l2[7][6]}{l2[7][7]}{l2[7][8]}{l2[7][9]}8')
    print(f'  9{l1[8][0]}{l1[8][1]}{l1[8][2]}{l1[8][3]}{l1[8][4]}{l1[8][5]}{l1[8][6]}{l1[8][7]}{l1[8][8]}{l1[8][9]}9                             9{l2[8][0]}{l2[8][1]}{l2[8][2]}{l2[8][3]}{l2[8][4]}{l2[8][5]}{l2[8][6]}{l2[8][7]}{l2[8][8]}{l2[8][9]}9')
    print(f' 10{l1[9][0]}{l1[9][1]}{l1[9][2]}{l1[9][3]}{l1[9][4]}{l1[9][5]}{l1[9][6]}{l1[9][7]}{l1[9][8]}{l1[9][9]}10                           10{l2[9][0]}{l2[9][1]}{l2[9][2]}{l2[9][3]}{l2[9][4]}{l2[9][5]}{l2[9][6]}{l2[9][7]}{l2[9][8]}{l2[9][9]}10')            
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    return ''
def cria_mapa(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append([' ']*tamanho)
    return lista

def posicao_suporta(matriz, blocos, linha, coluna, orient):
    if linha < 0 or coluna < 0 or linha >= len(matriz) or coluna >= len(matriz):
        return False
    
    if orient == 'v':
        if linha + blocos > len(matriz):
            return False
        for i in range(linha, linha + blocos):
            if matriz[i][coluna] != ' ':
                return False
    elif orient == 'h':
        if coluna + blocos > len(matriz):
            return False
        for j in range(coluna, coluna + blocos):
            if matriz[linha][j] != ' ':
                return False
    return True

def aloca_navios(mapa, blocos):
    n = len(mapa)    
    while True:
        for b in blocos:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            
            if posicao_suporta(mapa, b, linha, coluna, orientacao):
                if orientacao == 'h':
                    for i in range(b):
                        mapa[linha][coluna+i] = 'N'
                else:
                    for i in range(b):
                        mapa[linha+i][coluna] = 'N'
            break

pais_computador = random.choice(list(PAISES.keys()))
print(" =====================================")
print("|                                     |")
print("| Bem-vindo ao INSPER - Batalha Naval |")
print("|                                     |")
print(" =======   xxxxxxxxxxxxxxxxx   ======= \n")
print('Iniciando o Jogo!')
print(f'Computador está alocando os navios de guerra do país {pais_computador}...')
print('Computador já está em posição de batalha!')

soma = 1
for k,v in PAISES.items():
    print(f'{soma}: {k}')
    for k2,v2 in v.items():
        print(f'    {v2} {k2}')
    soma += 1

while True:
    input_jogador = int(input('Qual o número da nação da sua frota? '))
    if input_jogador not in [1,2,3,4,5]:
        print('Opção inválida')
    else:
        pais_jogador = input_jogador
        break

i = 0
for k , v in PAISES.items():
    i+=1
    if i == pais_jogador:
        pais_jogador_nome = k
        print(f'Você escolheu a nação {pais_jogador_nome}')
        print("Agora é sua vez de alocar seus navios de guerra!")
        break

mapa_computador = cria_mapa(10)
mapa_jogador = cria_mapa(10)
'''def mostrarMapa(mat1, mat2):
    for i in range(len(mat2)): 
        for l in range(len(mat2[i])): 
            if mat2[i][l] == "N": 
                cor = "V"
                mat2[i][l] = DICIONARIO_CORES[cor]
    print('   A   B   C   D   E   F   G   H   I   J        A   B   C   D   E   F   G   H   I   J')
    for linha in range(10):
        print(f'{linha+1:2d}', end='')
        for coluna in range(10):
            print(f' {mat1[linha][coluna]} ', end='')
        print(f'            {linha+1:2d}', end='')
        for coluna in range(10):
            print(f' {mat2[linha][coluna]} ', end='')
        print()
    print('   A   B   C   D   E   F   G   H   I   J        A   B   C   D   E   F   G   H   I   J')

#mostrarMapa(mapa_computador, mapa_jogador)'''

def aloca_navios_jogador(mapa, blocos,linha,coluna,orientacao):      
    if orientacao == 'h':
        for bloco in range(blocos):
            mapa[linha][bloco + coluna] = 'N'
    else:
        for bloco in range(blocos):
            mapa[linha + bloco][coluna] = 'N'
    return mapa

coords={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
def converte_coordenada(coordenada):
    letra = coordenada[0].lower()
    if len(coordenada) ==2: 
        coluna = int(coordenada[1])-1
    elif len(coordenada) == 3: 
        coluna = int(coordenada[1]+coordenada[2])-1
    for k,v in coords.items(): 
        if letra == k: 
            linha = v
    coordenada2 = [linha,coluna]
    return coordenada2

def valida_coordenada(letra, coluna):
    if letra.upper() in ALFABETO and int(coluna) in range(1,11):
        return True
    return False 

def converte_coordenada(l, c):
    letra = l.lower()
    coluna = int(c)-1
    for k,v in coords.items(): 
        if letra == k: 
            linha = v
    coordenada = [linha,coluna]
    return coordenada

def posicao_suporta_usuario(mapa, blocos,linha,coluna,orientacao):
    if orientacao=='h':
        if coluna+blocos>len(mapa[0]):
            return False
        for i in range(blocos):
            if mapa[linha][i+coluna]=='\u001b[32m▓▓▓\u001b[0m':
                return False
        return True
    elif orientacao=='v':
        if linha+blocos>len(mapa):
            return False
        for i in range(blocos):
            if mapa[linha+i][coluna]=='\u001b[32m▓▓▓\u001b[0m':
                return False
        return True

navios_usuario=[]
for k,v in PAISES[pais_jogador_nome].items():
    for k2 in range(v):
        navios_usuario.append(k)

navios_usuario_2=[]
for i in navios_usuario:
    navios_usuario_2.append(i)
print(navios_usuario)
del navios_usuario_2[0]
lista = cria_mapa(10)
for i in navios_usuario:
    while True:
        print(f'alocar: {i} {CONFIGURACAO[i]} blocos')
        sleep(1)
        if navios_usuario_2!=[]:
            print(f'próximos: {navios_usuario_2}')
        letra = input('Informe a letra:').lower()
        coluna = input('Informe a coluna:')
        direcao = input('Informe a orientação [v|h]').lower()
   
        if direcao in 'vh':
            if valida_coordenada(letra, coluna):
                if posicao_suporta_usuario(mapa_jogador, CONFIGURACAO[i], int(coluna)-1, coords[letra], direcao):
                    coordenada = converte_coordenada(letra, coluna)
                    mapa_jogador=aloca_navios_jogador(mapa_jogador, CONFIGURACAO[i], coordenada[1], coordenada[0], direcao)
                    print(printa_string(lista,mapa_jogador))
                    if navios_usuario_2!=[]:
                        del navios_usuario_2[0]
                    break
                else:   print('Opção inválida')
            else:   print('Opção inválida')
        else:   print('Opção inválida')

print("Iniciando Batalha naval!")
def jogador_perde(l):
    for i in range(len(l)):
        for k in range(len(l[i])):
            if l[i][k] == '\u001b[32m▓▓▓\u001b[0m' :return False
    return True

def comp_perde(l):
    for i in range(len(l)):
        for k in range(len(l[i])):
            if l[i][k] == 'N' :return False
    return True


while True:
    while True:
        linha = random.randint(0, len(mapa_jogador) - 1)
        coluna = random.randint(0, len(mapa_jogador[0]) - 1)
        if mapa_jogador[linha][coluna]=='   ':
            mapa_jogador[linha][coluna]='A'
            x="Água"
            break
        elif mapa_jogador[linha][coluna]=='\u001b[32m▓▓▓\u001b[0m':
            mapa_jogador[linha][coluna]='X'
            x="Fogo"
            break
    print(f'Computador ----->>>>> {numletra[coluna]}{linha+1} {x}')
    print(printa_string_bombardeio(lista,mapa_jogador,mapa_computador))
    if jogador_perde(mapa_jogador)==True:
        print("Você perdeu!")
        break
    while True:
        linha = input("Linha:")
        coluna = input("Letra:")
        if linha in lista_denumeros2 and coluna.lower() in letras:
            linha = int(linha)
            if mapa_computador[linha-1][d[coluna.lower()]]=='N':
                cria_mapa(10)[linha-1][d[coluna.lower()]]='X'
                mapa_computador[linha-1][d[coluna.lower()]] = "X"
                x='Fogo'
                break
            elif mapa_computador[linha-1][d[coluna.lower()]]=='   ':
                cria_mapa(10)[linha-1][d[coluna.lower()]]='A'
                x='Água'
                mapa_computador[linha-1][d[coluna.lower()]] ="A"
                break
            else:
                print(f"Posição {coluna.upper()}{linha} já bombardeada")
        else:
            print('Opção inválida')
    print(f'Jogador ----->>>>> {linha}{coluna} {x}')
    print(printa_string_bombardeio(lista,mapa_jogador,mapa_computador))
    if comp_perde(mapa_computador)==True:
        print("Você ganhou! Parabéns!")
        break
    
