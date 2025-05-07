nome_completo = ['Alexsandro', 'Matias']
# Neste exemplo, a variavel nome_completo
# está recebendo uma lista literal com os elementos Alexsandro e Matias
# Para criação de uma lista basta colocar os elementos dentro dos []
# separados ou não por vírgula. Neste momento, Python cria em memória uma lista
# que referencia a variável nome_completo. Isso é possível
# perceber através de:
#
# print(type(nome_completo)) - <class 'list'>

# Uma característica visível das listas é que elas são sequências mutáveis de elementos.
# Desta forma é possível alterar seus elementos, assim como sua estrutura interna.

#
# Métodos relevantes

# Adicionando termos a Lista
# nome_completo.append('Silva')

# Ordenando a lista de forma reversa
# nome_completo.sort(reverse=True)

# É visível que estes dois métodos, não retornam nenhum valor, mas alteram as estruturas internas da lista.
# Na verdade, eles retornam um valor None
# print(nome_completo.append('Santos'))

# Assim é possível adicionar qualquer tipo de objeto às listas,
# mesmo que esses valores sejam diferentes entre si
# constante = ['gravidade', 9.81, 10, 10j, len[1,3]]
# Isso somente é possível pq as listas guardam as referências para todos esses objetos que elas contém. Desta maneira,
# elas ficam armazenadas no runtime do Python. Sendo permitido até usar o slincing.
# print(nome_completo[:2])
# Com esse recurso é possível duplicar a lista nome_completo.
# Basta a atribuir uma cópia da lista para outra variável

# segunda_lista = nome_completo[:]
# print(segunda_lista)

# Porém, se fizermos
copia = nome_completo
# # Neste momento, a variável cópia vai ter a mesma referência que nome_completo, ou seja,
# # qualquer alteração que fizeremos em cópia, irá implicar em nome_completo
# copia.append('Santos')
# print(nome_completo)
# Outra forma de verificar se apontam para a mesma referência é usando a função builtin id
# print(id(copia), id(nome_completo))
# Até então apenas são exemplos de listas imutáveis como strings e números.
# Mas existe a possibilidade de manipularmos elementos mutáveis

# lista_externa = [1, 5, [7, 9, 6]]
# # Para acessar o último elementos de lista, que no caso é outra lista, segue da mesma forma:
# interna = lista_externa[-1]
# print(interna)
# interna.append(42)
# print(interna)
# print(lista_externa)
# Isso acontece por que apenas é manipulada a referência do último elemento da interna.
