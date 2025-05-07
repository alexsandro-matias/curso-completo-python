# Para definição de uma função em python usa-se a palavra reservada def.
# def funcao():
#     return 42
#
#
# # def nome_da_funcao(parâmetros):
# #     return corpo_da_funcao
#
# print(funcao())

# Como a representação de def - 'definition function' o interpretador vai ler as linhas de cima para baixo.
# Observa-se que a função não é executada, ela é apenas criada Depois disso, ou seja, no momento do print é
# que ele vai utilizar a função. Como já foi visto, como python utiliza a identação para definir escopo, caso
# a função esteja vazia, se faz necessária a palavra reservada pass para representar tal contexto.

# def funcao_vazia():
#     pass

# Assim, qualquer função em python sempre vai retorna algum valor, mesmo que não seja explicitado esse retorno.
# Caso não seja o valor retornado é none.

# print(funcao_vazia())

# Isso diferencia python de outras linguagens que explicita que não há retorno de algum
# valor da função explicitado pela palavra reservada void. No que tange os parâmetros, esses valores
# são passados dentro dos parênteses.

# def funcao(a, b, c):
#     print(a, b, c)
#
# funcao('alexsandro', '19', '84')

# Essa forma de passagem de parâmetros é chamada de passagem posicional, uma vez que a ordem dos parâmetros "bate"
# com a posição dos valores passados. Outra forma de passar parâmetros é de forma nomeada:
# def funcao(letra, dia, ano):
#     print(letra, dia, ano)

# funcao(letra='a', dia=10, ano=87)

# Neste caso, no momento da passagem do parâmetro o que interessa é o identificador do parâmetro,
# e não ordem.
# funcao(ano=87, letra='b', dia=8)

# O python suporta também o valor default.


# def funcao(letra, dia, ano=2023):
#     print(letra, dia, ano)
#
# funcao(letra='A', dia=19)
#
# def funcao(letra, dia, ano=2023, *args):
#     print(letra, dia, ano, args)
#
#
# funcao('A', 19, 1994, 'Alexsandro', 'Matias')

# Essa sintaxe somente é possível por que o python sabe quantos parâmetros que uma função tem.
# e se foi chamada uma função e os parâmetros foram nomeados, então é possível fazer essa diferenciação. Mas se houver
# a necessidade da passagem indefinida da quantidade de parâmetros, utiliza-se o operador posicional *args.
# Esse identificador, não é obrigatório, isto é, o nome args é apenas uma convenção da comunidade Python.
# Mas essa forma de passagem de parâmetros causa um efeito que os restante dos parâmetros ficam contidos numa tupla.
# saída da linha de cima - A 19 1994 ('Alexsandro', 'Matias'). Porém para que essa passagem indefinida de
# parâmetros seja nomeada, é necessário o uso de ** (dois asterísticos).

# def funcao(letra, dia, ano=2023, **kwargs):
#     print(letra, dia, ano, kwargs)
#
#
# funcao(letra='A', dia=19, ano=1994, nome='Alexsandro', sobrenome='Matias')
# Já neste caso os valores que sobraram, ou seja, aqueles que não correspondente na função,
# ficarão em um dicionario ao invés de uma tupla. Mesmo assim, a passagem não torna obrigatória a passagem nomeada.

# def funcao(letra, dia, ano=2023, **kwargs):
#     print(letra, dia, ano, kwargs)
#
#
# funcao('A', 19, ano=1994, nome='Alexsandro', sobrenome='Matias').

# Ainda é possível mesclar ainda mais o *args e o **kwargs

# def funcao(letra, dia, ano=2023, *args, **kwargs):
#     print(letra, dia, ano, *args, kwargs)
#
#
# funcao('A',16,1990,'Alexsandro','Matias', casado=True, graduado=True)
#  A partir do python 3, foi criada uma funcionalidade da linguagem chamada keyword only arguments.
#  Ele é o argumento que é obrigado a passar. Por exemplo entre o args e kwargs:

# def funcao(letra, dia, ano=2023, *args, x, y, **kwargs):
#     print(letra, dia, ano, args, kwargs)
#
# funcao('A',16,1990,'Alexsandro','Matias', casado=True, graduado=True)

# O seguinte erro será lançado -   funcao('A',16,1990,'Alexsandro','Matias', casado=True, graduado=True)
# TypeError: funcao() missing 2 required keyword-only arguments: 'x' and 'y'.

# Esses dois parâmetros se tornam obrigatórios e são incorporados como posicionais. Esses valores
# se tornam importantes quando se deseja deixar valores padrão de configuração.
# def funcao(letra, dia, ano=2023, *args, preguicoso=True, dorminhoco=True, **kwargs):
#     print(letra, dia, ano, preguicoso, dorminhoco, args, kwargs)
#

# Algo similiar ocorre no Django quando ele imprime as consultas de banco de dados, utilizando a função filter.
# Essa função recebe um dicionário divindindo-o através do '__'.

# def filter(**lookups):
#     for chave, valor in lookups.items():
#         print(chave.split('__'), valor)
#
#
# filter(name__start='Nome',
#        age__meio=30,
#        cidade__final='Romeu')

# Aprimorando o conceito, é possível criar uma função extremamente genérica utilizando apenas o args e kwargs.

# Essa função aceita qualquer tipo de parâmetro.
# def funcao(*args, **kwargs):
#     print(args, kwargs)
#
#
# tupla = 19, 10
# nome_completo = {'nome': 'Alexsandro', 'sobrenome': 'Matias'}

# funcao('a', teste='qualquer')

# passando os dois elementos para a função genérica, teremos como saída:
# funcao(tupla, nome_completo)
# saída - ((19, 10), {'nome': 'Alexsandro', 'sobrenome': 'Matias'}) {}.
# Assim teremos a tupla como parâmetro posicional, assim como teremos o dicionário também como parâmetro
# posicional apenas do args - já temos na saída - (tupla, dicionário). Para segregar para que a tupla fique em args
# e o dicionário ficasse **kwargs. Para isso teria que explicitar para cada elemento:

# funcao(tupla[0], tupla[1], primeiro_nome = nome_completo['nome'], segundo_nome = nome_completo['sobrenome'])

# Obviamente que o código acima não está Pythonico que seria utilizar índices para acessar sequencias.
# Num contexto mais prático, usamos o desempacotamento de forma nomeada para realizar a atribuição desses itens:
# funcao(*tupla, **nome_completo)


# def adicionar(a, b):
#     return a + b


# print(type(funcao))
# como funções são objetos em python. Ela possuem atributos e métodos. Então propriedades das
# mais diversas formas podem ser acessadas pela existência do atributo especial __code__.
# print(adicionar.__code__)
#
# # Assim, números de argumentos, bytecodes dentre outras informações podem ser acessadas através desse objeto.
# print(adicionar.__code__.co_argcount)
# print(adicionar.__code__.co_code)
# print(adicionar.__code__.co_names)
# print(adicionar.__code__.co_varnames)

# Até mesmo é possível fazer o disambler dessa função importando a função 'dis'
# import dis
#
# print(dis.dis(adicionar))

# Caso haja necessidade de criar uma documentação da método,
# existe um conceito chamado de docstring que já método de documentação do módulo,
# é criada a documentação através do __doc__.
def adicionar(a, b):
    'O método soma duas varíaveis.'
    return a + b

# print(adicionar.__doc__)
#
# # Esse apoio da linguagem também pode ser visto no help do módulo.
# help(adicionar)

# Outra vantagem de funções serem objetos é que elas podem ser parâmetros para outras funções.

def operacoes(operacao, a, b):
    return operacao(a, b)


print(operacoes(adicionar, 2, 4))


# Dinamicamente, o python vai verificar o objeto adicionar e verificar que ele é um objeto do tipo função e que recebe
# dois parâmetros que serão somados e depois retornados, e posteriormente retornados para a função somar.
# A mesma coisa acontecer para a multiplicação

def multiplicar(a, b):
    return a * b


operacoes(multiplicar, 2, 3)