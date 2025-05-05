# Desafio - crie um programa que:
# - Pede por usuário e uma senha.
# - Se ambos forem corretos, exibe uma msg de sucesso.
# - Caso contrário, exibe uma msg de erro. A mgs é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variáveis dentro do próprio código.

usuario_correto = 'Pedro'
senha_correta = 'senha secreta'

print('------ INÍCIO ------')

usuario_correto = input('Digite seu usuário: ')
if usuario_correto == 'Pedro':
    senha_correta = input('Digite sua senha: ')
    if senha_correta == 'senha secreta':
        print('Logado com SUCESSO')
    else:
        print('Senha incorreta')
else:
    print('ERRO, usuário incorreto!')

print('------ FIM ------')


# cola do curso (operadores de comparação)

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Acesso liberado, seja bem-vindo {usuario}!')
    else:
        print(f'Senha incorreta para o usuário {usuario}.')
else:
    print(f'Usuário {usuario} não cadastrado no sistema!')


# cola do curso (operadores booleanos)

usuario = input('Nome de usuário: ')
usuario_esta_correto = usuario == usuario_correto
senha_esta_correta = input('Senha: ') == senha_correta

if usuario_esta_correto and senha_esta_correta:
    print(f'Acesso liberado, seja bem-vindo {usuario}!')
if usuario_esta_correto and not senha_esta_correta:
    print(f'Senha incorreta para o usuário {usuario}.')
if not usuario_esta_correto:
    print(f'Usuário {usuario} não cadastrado no sistema!')
