# Dicionários são hashmaps, ou seja armazenam um conjunto de dados com chave e valor.
# Para criação de um dicionário se usa as chaves {}

dicionário = {'nome': 'Alexsandro', 'ano_nascimento': 1984, 'sobrenome': 'Matias'}
# Neste caso, nome é a chave e Alexsandro é valor.
# A ordem de impressão da informação não é necessariamente a mesma do que foi atribuído,
# uma vez que cada chave é calculado através de hash do python.
# print(dicionario)
# Para acessar uma chave de um dicionário, se utiliza o [] só que ao invés de passar um índice, usa-se o nome da chave.
# print(dicionário['nome'])
# Mas se tentar acessar uma chave que não existe, o Python vai lançar uma exceção de keyerror.
# print(dicionario['chave'])
# print(dicionario['chave'])
#           ~~~~~~~~~~^^^^^^^^^
# KeyError: 'chave'

# Para verificar se existe uma chave no dicionário basta usar e o operador in no dicionário:
# print('chave' in dicionário)
# print('nome' in dicionário)
# Já para os valores, usa-se o método values().
# print('Alexsandro' in dicionário.values())
# print('Renato Russo' in dicionário.values())

# Para utilizar a busca que não lança um erro, usa-se o método get. Ele não retorna o erro.
# Mas quase não encontre, retorna None.
# print(dicionário.get('chave'))
# Existe a possibilidade, de caso o valor não seja encontrado, o Python retornar um valor padrão.
# print(dicionário.get('Chave', 'Chave não encontrada'))
# print(dicionário.get('nome', 'Chave não encontrada'))

# Para descobrir a quantidade chaves que há no dicionário, usa-se a função builtin len().
# print(len(dicionário))

# A partir do Python 3, existe uma ferramenta chamada dictionary view que retorna objetos em dinâmicamente das chaves,
# dicionários ou ambos:

# # Chaves
# print(dicionário.keys())
#
# # valores
# print(dicionário.values())
#
# # par chave-valor, que neste caso retorna tuplas que representam as chaves mais os valores.
# print(dicionário.items())

# # Segregando os dicionários em variáveis:
chaves = dicionário.keys()
valores = dicionário.values()
itens = dicionário.items()
#
#
# # Adicionado uma chave ao dicionário:
dicionário['sexo'] = 'Masculino'
#
#
# # Verificando novamente as chaves
# print(chaves)
# print(valores)
# print(itens)
#

# É perceptível que as dictionary views são alterados quando um dicionário é alterado.
# Para não quer este comportamento, é necessário que seja convertido cada item deste numa tupla
# chaves = tuple(dicionário.keys())
valores = tuple(dicionário.values())
#
# # Aqui será uma tupla de tuplas que armazena a chave e valor
# itens = tuple(dicionário.items())

# Caso haja a necessidade de deletar uma chave do dicionário, usa-se o comando del
# del dicionário['sexo']
# print(dicionário)
#

# Como os dicionários são hashmaps, as chaves precisam ser imutáveis. Assim, por exemplo,
# caso seja atribuída uma lista como chave, daria um erro de  - unhashable type: list
lista = [1, 2, 3]
# dicionário[lista] = 'Vai dar errado'

# Como esse hash utiliza esse valor calculado,
# é a partir dele que o interpretador sabe como encontrar o par chave-valor.
# Agora, se o valor fosse mutável, o Python não teria como garantir que os valores possam ser encontrados.
# A função builtin que faz esse trabalho é hash e também é ela que lança esse erro, ou seja, o mesmo erro.
# print(hash(lista))
# Já com uma tupla, o resultado é diferente.
# print(hash(valores))
#
# # Como strings também são imutáveis, também pode ser aplicada o hashmap.
# print(hash('João'))
#
# # Outra forma de adicionar uma chave ao dicionário é através do método update.
# dicionário.update(compras=['mouse', 'teclado'])
# # print(dicionário)
# #Como o valor é uma lista, esse valor está passível de alteração.
# dicionário['compras'].append('monitor')
# print(dicionário)
# # Para apagar o elemento, e ao mesmo tempo, retorná-lo usa-se o método pop
# dicionário.pop('compras')
# print(dicionário)

# Caso haja um conjunto de dados que é tupla de tuplas, caso haja a conversão em um dicionário,
# o python percebe e faz essa conversão de forma suave.
tupla = tuple(dicionário.items())
print(tupla)
tupla = dict(tupla)
print(tupla)
