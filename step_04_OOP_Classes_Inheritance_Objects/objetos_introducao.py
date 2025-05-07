# para representar um literal binário usa-se o o termo 0b e a sequencia binária.
# binario = 0b1000001
# letra = chr(binario)
# print(binario)
# print(letra)

# Então o mesmo valor em bits pode ser representado de formas diferentes dependendo do contexto.
#
# pessoas = ['alexsandro', 'maria', 'santos', 'josiane', 'josefa']
# # print(id(pessoas), type(pessoas))
#
# # quando o print() é chamado, o que está sendo impresso na tela realmente é o conteúdo do objeto 'pessoas'.
# # Da mesma maneira se for impresso o objeto com a função id() será impressa a identidade deste objeto.
# # Outra função que mostra mais características do objeto é a função type que, como o próprio nome sugere,
# # mostra o tipo dele. Assim, qualquer objeto tem características gerais um valor, tipo e uma identidade. Percebe-se
# # que os valores podem ser iguais em alguns contextos, mas caracterizam objetos diferentes.
#
# funcionarios = ['alexsandro', 'maria', 'santos', 'josiane', 'josefa']
# # print(id(pessoas))
# # print(id(funcionarios))
# # Mesmo possuindo os mesmos tipos e valores, a identificação dos objetos é diferente, ou seja,
# # são listas totalmente distintas. Para provar que os valores são iguais, basta usar o operador ==
# # print(funcionarios == pessoas)
# # Agora, para verificar se identidade de uma é igual a outra, o operador utilizado deve ser o 'is'.
# print(funcionarios is pessoas)

# A forma de declaração de classes em python é através da palavra reservada class.
# class Car: pass
# # A partir deste momento, já existe em memória um objeto do tipo class. Isso fica evidente da seguinte forma:
# print(Car)
# # Em outras palavras a palavra Car representa uma variável sendo executada em runtime em memória.
# # Para instanciar uma classe, basta digitar o nome da classe e depois parentesis - Car()
#
# print(Car())
# # saída <__main__.Car object at 0x0000027438530950> - que será a identidade da variável do tupo car.


from math import sqrt

a = 2
b = 4
c = 8

variavel = a ** 2 + 3 / 4 * b * 987 * (c - ((10 ** -9) / sqrt((0.5 ** 3))))

variavel = variavel % 23691

print(variavel)
