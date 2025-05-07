# O while se baseia na estrutura de repetição que enquanto uma condição for verdadeira,
# uma ação ou um conjuto de ações deverá ser repetida.
nome = 'Alexsandro'
# Uma forma de acessar cada letra do nome:
# i = 0
# while i < 10:
#     print(nome[i])
#     i = i + 1
#
# Outra forma de incremetar é através do operador aumentado
# i = 0
# while i < 10:
#     print(nome[i])
#     i += 1
# Obviamente esse código não é nem de perto ideal, uma vez que alterado o tamanho da variável nome,
# este programa vai se comportar de forma totalmente diferente.
# Para fixar a repetição pelo tamanho da string, iremos usar a função len().
# i = 0
# while i < len(nome):
#     print(nome[i])
#     i += 1

# Mas quando é sabido a quantidade de vezes que essas repetições irão ocorrer,
# a estrutura de repetição mais indicada é o for.

# for i in range(len(nome)):
#     print(nome[i])

# A função range é uma função builtin do python que retorna um intervalo.
# Assim, a função range retorna um range object.
# print(type(range(8)))
# Da mesma forma, é possível acessar cada item desse intervalo através dos seus índices.
# intervalo = range(4)
# print(intervalo[2])

# Com o uso do range, os elementos ficam representados por apenas 1 elemento em memória,
# diferentes se os valores fosse colocados em uma lista que ocupariam um número maior em memória.

# print(range(1, 20))
# # Colocando na lista
# lista = list(range(1, 20))
# print(lista)

# Do mesmo modo que o slicing, aqui é possível colocar o passo como o terceiro parâmetros
# lista = list(range(0, 20, 2))
# print(lista)
# Neste exemplo é possível imprimir apenas os números pares entre 0 e 20.
# O também pode ser representado da seguinte forma:
# for i in range(0, 20, 2):
#     print(i)
#
# como o range retorna uma sequência, e como na sintaxe do for ele espera um interável representado por:
# for VARIÁVEL_DE_CONTROLE in ITERÁVEL:
#     CORPO_DO_FOR_
#     UTILIZANDO A VARIÁVEL_DE_CONTROLE

# Como as strings também são iteráveis, ou seja, uma sequência de letras,
# o uso do for também pode ser utilizado neste contexto.
# for letra in nome:
#     print(letra)
# Assim, de forma geral, o python provê forma de alto nível para manipulação e acesso de índices de sequencias.
# Por exemplo, caso seja necessário o acesso ao índice, existe a palavra reservada enumarate que faz essa função.

# for letra in enumerate(nome):
#     print(letra)
# Neste caso, o que é retornado a cada iteração é uma tupla contendo no primeiro item o índice da iteração,
# enquanto que o segundo é o elemento desta iteração. Caso não queria uma tupla para esta manipulação,
# essa separação pode ser feita diretamente no ciclo for.

# for indice, letra in enumerate(nome):
#     print(indice, letra)

# O enumarate quando é chamado, ele retorna um objeto iterável enumarate.
# sequencia = enumerate(nome)
# print(sequencia) - <enumerate object at 0x0000020AF5227330>
# Todos iterator implementa o método chamado de __next__() que controla cada item da iteração.
# Mas quando chegar ao último elemento, ele interrompe o ciclo de forma de alto nível.
# Algo que outras linguagens é chamado de foreach(). Da mesma forma que em outras linguagens,
# as palavras reservadas continue e break estão presentes. Vamos supor que precisemos que a letra 'e' não seja impressa.


# for indice, letra in enumerate(nome):
#     if letra == 'e':
#         continue
#     print(indice, letra)

# E de forma similiar a outras linguagens, o comando continue para o restante do código passa para a próxima iteração.
# Já interroper a iteração de forma completa, como em outras linguagens é o comando break:

# for indice, letra in enumerate(nome):
#     if letra == 'e':
#         break
#     print(indice, letra)