def sacar():
    print('DIA - R$30,00')
    print('KM - R$0.10')
    cnh = input('cliente possue cnh?')
    if cnh != 'sim':
        print('logue alguem que tenha cnh - invalido-')
        return False
    
    cnh_number = input('cnh: ')
    nome= input('nome: ')
    
    cpf = input('cpf: ')
    placa = input('Placa: ')
    days = float(input('Dias: '))
    km = float(input('km '))
    total = (days *30) + (km*0.10)

    print('-'*15)
    print(f'{nome},{cpf},{cnh_number}')
    print(f'Total a pagar: {total}')
