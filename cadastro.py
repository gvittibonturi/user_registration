# Programa: Cadastro.py
# Descrição: Cadastro de usuários em Python 
# Data: Abril de 2025

import random
from datetime import datetime

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']

usuarios = []

class User():
    """Classe que cria e define o usuário de um sistema"""

    def __init__(self, nome, idade, data_aniversario, data_cadastro):
        """Inicializa os atributos nome, idade, data_aniversario e data_cadastro"""
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario
        self.data_cadastro = data_cadastro

    def cadastrar_usuario(self):
        """Cadastra novos usuáriosem uma lista de dicionários"""   
        info_usuario = {'Nome': self.nome, 'idade': self.idade, 'data_aniversario': self.data_aniversario,
                        'data_cadastro': self.data_cadastro}
        
        usuarios.append(info_usuario)


while True:
    valor_nome = input('Digite o nome do usuário: ')    
    if valor_nome == 'q':
        print('Programa finalizado')
        print(usuarios)     
        break # Interrompe o laço se o usuário digitar 'q'

    try:
        valor_idade = (input('Digite a idade do usuário: '))
        str_aniversario = input('Digite a data de aniversário: ')
        data_niver_convert = datetime.strptime(str_aniversario, '%d/%m/%Y') # registra a data digitada do aniversario do usuario e converte para TIME
        data_niver_br = data_niver_convert.strftime('%d/%m;%Y') # converte a variável 'data_niver_convert' para padrão brasileiro
        data_cad_convert = datetime.now().strftime('%d/%m/%Y') # registra a data do cadastro do usuário

        usuario_cadastrado = User(valor_nome, valor_idade, data_niver_br, data_cad_convert)
        usuario_cadastrado.cadastrar_usuario()
        
    except ValueError:
        print('Entrada inválida. Digite um nome válido.')

#     #print(f'Data do cadastro: {data_cadastro}')
#     #cartao_usuario = random.choice(cartoes)

else:
    print('Programa finalilzado')