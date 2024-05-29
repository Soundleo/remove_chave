pessoa = {
    'Nome': 'Leandro Peres',
    'Idade': 38,
    'Profissão': 'PO',
    'Empresa': 'BB',
    'Gênero': 'Masculino',
    'Cidade': 'Guará',
}

del pessoa [input('Informe o nome da chave a a ser deletada')]

for i in pessoa:
    print(f'{i}: {pessoa.get(i)}')
