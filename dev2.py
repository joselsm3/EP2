from random import choice
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}
pais_computador = choice(list(PAISES.keys()))
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
        print(f'Você escolheu a nação {k}')
        print("Agora é sua vez de alocar seus navios de guerra!")
        break




