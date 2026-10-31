# escola
#cadastro

#exe. aplicativo



acesso = input('Deseja acessar o sistema? s/n -- ')
while acesso ==  's': #isso vai verificar se e V ou F
    print('SISTEMA ESCOLA xyz')

    nome = input('Nome do aluno: >> ')#variável
    #snake-case
    nota_1 = float(input('Nota 1: >> '))
    nota_2 = float(input('Nota 2: >> '))
    nota_3 = float(input('Nota 3: >> '))

    #média do aluno

    lista = []
    lista.append(nota_1)
    lista.append(nota_2)
    lista.append(nota_3)

    media = sum(lista)/len(lista)

    print('O aluno(a)', nome, 'possui a média', media)

    if media >= 7:
        print(f"O {nome} passou de ano ✔")
    elif media >= 5 and media < 7:
        print(f"O {nome} está de recuperação ‼")
    else:
        print(f"O {nome} não passou de ano ❌")
    acesso = input('Deseja continuar? s/n >> ')

print('Até logo...')
input('clique enter para sair...')