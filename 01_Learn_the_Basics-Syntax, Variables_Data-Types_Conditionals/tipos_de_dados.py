# No python a tipagem de dados é dinâmica. Ou seja, em tempo de execução o python verifica os tipos.
# Se tivermos a variável sendo declarada como no exemplo abaixo:
# letras = 'alex'
# O python não tem nenhuma indicação qual o tipo da variável letras. Assim o interpretador
# "descobre" dinamicamente pelo conteúdo de letras o seu contúdo, e como encontrar os métodos.
# print(letras.upper())

# Destrichando o código:

# letras - identificador da variável ou o nome que será referenciado nas vezes que essa variável poderá ser utilizada.
# Neste momento, o Python identifica que letras se trata de objeto do tipo string
# . (ponto) - acessor - permite acessar o que está dentro do objeto - funções e atributos.
# Método chamado acessado pelo objeto do tipo string.

# print(letras.upper)
# - <built-in method upper of str object at 0x0000022ADC0D6EB0>

# Além de ser uma linguagem de tipagem dinâmica, ela também é uma linguagem de tipagem forte.
# Assim, uma vez que a varíavel é identificada com um tipo, não é possível fazer a
# conversão implícita daquele dado em outro.
# print('1' + 1)
# Traceback (most recent call last):
#   File "C:\Users\almei\github-repositorios\base_python\tipos_de_dados.py", line 21, in <module>
#     print('1' + 1)
#           ~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# Como se trata de uma ambiguidade, esse erro é gerado.
# Por que não é possível saber se é para concatenar duas letras 1 ou se é para somar o número 1 com outro 1.
# Para resolver podemos fazer de duas formas:
#
# numeros = 1 + int('1')
# # Neste caso, a função int recebe o texto '1'.
# Depois converte este texto para o número 1 e depois cria um novo objeto.
# # Depois soma-se o número 1 e outro número 1.
# # Isso somente é possível por que a função int() sabe trabalhar com texto que possue apenas números.
#
# letras = str(1) + '1'
# # Da mesma forma ocorre neste exemplo, mas no sentido inverso. Isto é, ele recebe um número 1.
# # Depois converte para string e depois cria um novo objeto do tipo string e concatena com o outro caractere 1
#
# print(letras, numeros)

# Com esses dois exemplos, foi possível verificar um conceito de sobrecarga de operadores.
# No primeiro caso, o sinal de '+' tem a função de somar dois números. Já na variável letras o
# mesmo sinal tem a função de concatenar (juntar) strings. Essa funcionalidade é feita por um açucar sintático.
# Por que o método real que é implementado é __add__()
# letras = '1'.__add__(str('1'))
# print(letras)
#
# numeros = int('1').__add__(1)
# print(numeros)

# A mesma sobrecarga ocorre com símbolo de '*' que pode multiplicar um número ou replicar (repetir) uma string.
# print(3 * 2)
# print("* " * 2)

# Que representa da mesma forma com o método __mul__()
# numero = int(3).__mul__(2)
# print(numero)
# impressao = '# '.__mul__(2)
# print(impressao)

# Pode-se encarar que a partir do tipo de dado que está sendo operado a semântica do operador se adapta à operação.
# Outro exemplo é o operador % que pode representar o resto da divisão inteira
# resto_divisao = 3 % 2
# print(resto_divisao)
# # Esse método também pode ser utilizado diretamente da classe.
# resto_divisao = int(3).__mod__(2)
# print(resto_divisao)

# Mas se há também a possibilidade utilizar juntamente com strings.
# nome_completo = 'Alexsandro %s' % 'Matias'
# print(nome_completo)
# Já neste caso, o python faz um processo chamado de interpolação -
# o que é próximo do printf do C - que a partir de
# uma posição ele substitue a variável pelo identificado na mesma ordem - spaceholder.
# Essa abordagem não se torna tão intuitiva quando se começa a usar mais variáveis.
# Podemos também utilizar tuplas para preencher esses spaceholders:
# nome_completo = '%s %s' % ('Alexsandro', 'Matias')
# print(nome_completo)
# Realizando a sobrecarga, usaremos o método especial:
# nome_completo = '%s %s.'.__mod__(('Alexsandro','Matias'))
# print(nome_completo)
