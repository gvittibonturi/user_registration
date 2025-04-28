# Programa de cadastro de usuários e sorteio de cards com valor

import random
from datetime import datetime

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']

usuarios = []
#info_usuario = {}

while True:
    valor_nome = input('Digite o nome do usuário: ')
    if valor_nome == 'q':
        print('Programa finalizado')
        print(usuarios)
        break # Interrompe o laço se o usuário digitar 'q'

    try:
        valor_idade = (input('Digite a idade do usuário: '))
        #str_aniversario = input('Digite a data de aniversário: ')
        #data_aniversario = datetime.strptime(str_aniversario, '%d/%m/%Y')
        #info_usuario['aniversario'] = data_aniversario 
        #data_cadastro = datetime.now().strftime('%d/%m/%Y') # registra a data do cadastro do usuário
        #info_usuario['dt_cadastro'] = data_cadastro

        info_usuario = {'Nome': valor_nome, 'idade':valor_idade}
        usuarios.append(info_usuario)

    except ValueError:
        print('Entrada inválida. Digite um nome válido.')

    #print(f'Data do cadastro: {data_cadastro}')
    #cartao_usuario = random.choice(cartoes)
else:
    print('Programa finalilzado')



'''
nome_busca = input('Digite o nome que deseja buscar: ')
for i in range(0, len(usuarios)):
    user = usuarios[i]
    print(user)
'''