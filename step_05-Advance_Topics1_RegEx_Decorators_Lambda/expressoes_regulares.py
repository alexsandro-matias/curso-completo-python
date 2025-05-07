# Expressões Regulares é uma linguagem que reconhece padrões (pattern) aplicado a um texto. Isso
# facilita a extração de características padronizadas em textos. Para isso, existe um módulo chamado 're'
# - Regular Expressions. Como já visto antes, para importar este módulo:
import re
# Com essa importação, se torna possível funções importantes como , por exemplo, busca de padrões no texto.
# print(re.match('abc', 'abc'))
# <re.Match object; span=(0, 3), match='abc'>.
# Esse retorno é um objeto do tipo Match que retorna padrões, no span é que posição ele encontrou texto, ou seja,
# da posição 0 até a posição 3. Mas há limitação nesta função, uma vez que ela procura uma função apenas no início do
# texto. Caso não encontre, ela retorna None.

# print(re.match('abc', 'alexsandroabc'))
# Para procurar em toda extensão do texto, devemos procurar com a função search.
# print(re.search('abc', 'alexsandroabc'))
#
# Já para procurar todas as ocorrências, usaremos o método findall.
#
# print(re.findall('a', 'alexsandro'))
# print(re.findall('abc', 'alex_abc_sandro_abc'))

# Para evitar a repetição para invocar o módulo re o tempo inteiro, iremos apenas invocar os métodos desse objeto.

from re import findall

# Mesmo usando esses métodos, o uso apenas do conjunto pequeno de caracteres possa ser que não atenda totalmente a
# resolução das demandas gerais dos programadores. No python, expressões regulares suportam o uso de metacaracteres
# representados pelo '.'
# print(match('.', 'abc')) - <re.Match object; span=(0, 1), match='a'>
# Ou seja, ele encontrou o caracterer 'a' na posição inicial. Assim esse ponto representa qualquer caracter,
# exceto '\n'.
# print(match('.', '012'))
# # - <re.Match object; span=(0, 1), match='0'>
# # Espaço em branco
# print(match('.', ' '))
# # - <re.Match object; span=(0, 1), match='a'>
# #
# #
# # Tabulação ou caracterer t com escape ou escapado
# print(match('.', '\t\t'))
# # - <re.Match object; span=(0, 1), match='\t'>
#
# Já com de quebra de linha:
# print(match('.', '\n'))
# Neste caso ele retorna None, mas se for qualquer coisa diferente do quebra de linha,
# a saída vai ser algo parecido que o comando match.
# print(search('.', 'abc'))
# Como o '.' tem uma função coringa, caso executar a função findall()
# e irá retornar se o padrão vai ter com o primeiro elemento - True, segundo elemento - True.
# Então irá retornar todos os elementos numa lista.
# print(findall('.', 'abc'))

# Outros metacaracteres importantes são chamados âncoras que são aqueles que representam o início e o final do texto.
# print(findall('^.', 'alexsandro\nmatias\n'))
# # Neste caso acima, somente será retornado apenas o primeiro caractere da string.
# # Mas se for passado um terceiro parâmetro chamado (flag) de quebra de linha teremos:
# print(findall('^.', 'alexsandro\nmatias\n', re.MULTILINE))
# Neste segundo caso, a âncora vai retornar a cada quebra de linha uma primeira linha.

# Já a âncora de final de linha ou da string.
print(findall('.$', 'alexsandro\nmatias\n', re.MULTILINE))
# A mesma coisa acontece neste contexto, mas ao invés de ser o primeiro caracter, neste será o último.
