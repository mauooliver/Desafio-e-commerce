# ***Crie um sistema de e-commerce, onde o usuário possa:***
# *Utilize variáveis, listas, condicionais*
# Foco resolver o problema
# Vamos trabalhar:
# ***Criatividade | Pensamento lógico | Flexibilidade cognitiva***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***

print(' Seja bem vindo(a): A Sua loja.com')
print('---' * 9)
print('Realize seu cadastro, para continuar')

cadastro = {
    'nome':'Nome',
    'idade' : 0,
    'CPF' : 0,
    'endereço' :'Nome',
    'crie_login' :'Nome',
    'crie_senha' : 0
}

seu_nome = input('Seu Nome: ')
sua_idade = int(input('Sua Idade: '))
seu_CPF = int(input('Digite seu CPF: '))
seu_endereço = input('Seu endereço: ')
crie_um_login = input('Crie seu login: ')
crie_sua_senha = int(input('Crie sua senha: '))

cadastro['nome'] = seu_nome 
cadastro['idade'] = sua_idade
cadastro['CPF'] = seu_CPF
cadastro['endereço'] = seu_endereço
cadastro['crie_login'] = crie_um_login
cadastro['crie_senha'] = crie_sua_senha

print('---' * 9)
print('Cadastro criado, coloque Login e Senha para acessar')
print('---' * 9)

login = input('Digite seu login: ')
senha = int(input('Digite seu senha: '))


if login == cadastro['crie_login'] and senha == cadastro['crie_senha']:
    print('Acesso autorizado')  
    print('---' * 9)
    
    print('Produtos disponiveis')
    lista_prod =  ['camisa', 'calça', 'blusa', 'bone']
    lista_preço = [  80.00   ,   159.00 ,   170.00 ,   55.00 ]
    
    print(lista_prod)
    print(lista_preço)

    print('---' * 9)
    meu_carrinho = []
    
    prod1 = int(input('Escolha a partir do indice: '))
    prod2 = int(input('Escolha a partir do indice: '))
    prod3 = int(input('Escolha a partir do indice: '))
    prod4 = int(input('Escolha a partir do indice: '))
    
    meu_carrinho += (lista_prod[prod1], lista_prod[prod2], lista_prod[prod3], lista_prod[prod4] )
    total        = (lista_preço[prod1], lista_preço[prod2], lista_preço[prod3], lista_preço[prod4])
    soma = sum(total)
    
    print('---' * 9)
    print('Minhas compras: ', meu_carrinho)
    print('---' * 9)
    print('Total a pagar R$', round(soma,2))
    print('---' * 9)
    pagamento = ['Dinheiro','Cartão','PIX']
    print('Escolha uma forma de pagamento: ', pagamento)
    print('---' * 9)
    pag1 = int(input('Escolha a partir do indice: '))
    print('---' * 9)
    pag = {
        'forma' : 0,
    }
    pag['forma'] = pag1
    print(pag)

else:
    print('Acesso negado, Senha ou login errado')

print('---' * 9)
print('A Sua Loja.com Agradece, volte sempre')

