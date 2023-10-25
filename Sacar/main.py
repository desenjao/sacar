from login import login
from sacar import sacar
while True:
    username = input('usuario: ')
    password = input('Senha: ')

    if login(username, password) == True:
        sacar()
        refresh =input('deseja continuar sacar?')
        if refresh != 'sim':
            break
    else:
        print('usuario invalido')    

'''''

def login(user, passwd):
    if user in usuarios and passwd in senhas:
        return True
    else:
        return False

user = input("Digite o nome de usuário: ")
passwd = input("Digite a senha: ")

if login(user, passwd):
    print("Logado com sucesso!")
else:
    print("Usuário ou senha incorretos!")
    '''
