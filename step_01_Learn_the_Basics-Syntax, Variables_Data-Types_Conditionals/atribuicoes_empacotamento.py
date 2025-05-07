# Quando fazermos uma atribuição de vários itens separados por vírgula ","
# Essa atribuição será feita para uma tupla
primeira_pessoa = 'Alexsandro', 'Matias', 14, 7, 80
segunda_pessoa = 'Maria', 'Cícera', 19, 11, 77

pessoas = (primeira_pessoa, segunda_pessoa)


def descricao(texto):
    print(nome, sobrenome, ano_nascimento)
#
# Traceback (most recent call last):
#   File "C:\Users\almei\github-repositorios\base_python\main\.idea\atribuicoes_empacotamento.py", line 11, in <module>
#     descricao(nome_completo)
#   File "C:\Users\almei\github-repositorios\base_python\main\.idea\atribuicoes_empacotamento.py", line 7, in descricao
#     print(nome, sobrenome, ano_nascimento)
#           ^^^^
# NameError: name 'nome' is not defined. Did you mean: 'None'?

#
# Neste momento, dará um erro, já que nem nome, sobrenome e nem ano_nascimento
# foram definidos. Em Python é possível atribuição múltipla
# para passarmos de uma tupla para estes parâmetros da função. Então teremos:
#
# def descricao(texto):
#     nome, sobrenome, ano_nascimento = texto[0], texto[1], texto[2]
#     print(nome, sobrenome, ano_nascimento)

# Mas obviamente, este código não está pythônico o suficiente,
# uma vez que temos três elementos e na função atribuimos os três elementos da tupla.
# Isso somente é possível por que o Python sabe a quantidade de termos da tupla. Então, é possível
# passar apenas a tupla:
# def descricao(texto):
#     nome, sobrenome, ano_nascimento = texto
#     print(nome, sobrenome, ano_nascimento)

# No exemplo acima, O interpretador cria um "match" com a ordem da tupla com a ordem dos termos.
# Agora supor que queiramos apenas o nome e sobrenome vai subir um
# erro dizendo que há mais argumentos para desempacotar:


# def descricao(texto):
#     nome, sobrenome = texto
#     print(nome, sobrenome, ano_nascimento)
# Erro:   File "C:\Users\almei\github-repositorios\base_python\main\.idea\atribuicoes_empacotamento.py",
# line 39, in descricao
#     nome, sobrenome = texto
#     ^^^^^^^^^^^^^^^
# ValueError: too many values to unpack (expected 2)

# Uma forma de contornar isso é representar de forma explícita quais termos devemos atribuir:

# def descricao(texto):
#     nome, sobrenome = texto[0], texto[1]
#     print(nome, sobrenome)
#

# A mesma coisa acontece com slicing
# def descricao(texto):
#     nome, sobrenome = texto[0:2]
#     print(nome, sobrenome)

# Até agora a atribuição feita numa determinada ordem, mas para pegarmos o primeiro e último item, teremos:
# def descricao(texto):
#     nome, ano_nascimento = texto[0], texto[2]
#     print(nome, ano_nascimento)

# Mas para facilitar a ordem da atribuição,
# quando se deseja descartar um valor atribuído, o símbolo é underscore - "_",
# ou seja, Normalmente se coloca para uma variável que não será usada. Em outras palavras o _ é como se
# fosse uma variável qualquer.
# def descricao(texto):
#     nome, _, _ = texto
#     print(nome, _, _)

# Mas se houverem muitas variáveis entre as variáveis desejadas, ao invés de usar várias _,
# pode-se usar o asterísticos para representar o restante das variáveis.
# def descricao(texto):
#     nome, *_, ano= texto
#     print(nome, _, ano)

# Porém nessa abordagem, a impressão será  - Alexsandro ['Matias'] 1984 - isto é,
# o primeiro, o último e uma lista com o restante dos itens. O que terá uma abordagem diferente
# se for feita descrita:
def descricao(texto):
    *nome, _, ano = texto
    print(nome, _, ano)


# Como nome está com "*", esta variável que será guardada numa lista até encontrar alguma variável
# explicitada para depois ser atribuída - ['Alexsandro', 'Matias', 19] 10 84

# if __name__ == '__main__':
#     descricao(nome_completo)


# Utilizando para mostrar a interação antes do desempacotamento:
# for pessoa in pessoas:
#     print(pessoa)

# Utilizando com desempacotamento (unpacking)
for nome, sobrenome, *_, ano in pessoas:
    print(nome, sobrenome, _, ano)
