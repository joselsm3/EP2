import random
from constantes import CONFIGURACAO, PAISES, ALFABETO, CORES

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
    print(mapa)
    return mapa

def foi_derrotado(matriz):
    for l in matriz:
        for c in l:
            if c == 'N':
                return False
    return True

sorteio = random.choice(list(PAISES.keys()))
print(" =====================================")
print("|                                     |")
print("| Bem-vindo ao INSPER - Batalha Naval |")
print("|                                     |")
print(" =======   xxxxxxxxxxxxxxxxx   ======= \n")
print('Iniciando o Jogo!')
print(f'Computador está alocando os navios de guerra do país {sorteio}...')
print('Computador já está em posição de batalha!')

soma = 1
for k,v in PAISES.items():
    print(f'{soma}: {k}')
    for k2,v2 in v.items():
        print(f'    {v2} {k2}')
    soma += 1