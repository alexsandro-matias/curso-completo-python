# as strings são sequências em python. Assim como exemplo abaixo:
nome = 'Alexsandro'
# Se pegarmos qualquer elemento da string acima, não será um char, e sim uma string.
# Ou melhor é retornado o primeiro elemento de uma sequência de nome
# print(type(nome[0]))

# Erro por tentar acessar um índice que ultrapassa a faixa da sequência.
# print(nome[10])

# Para acessar a última posição da sequência:
# print(nome[len(nome) - 1])

# Porém a forma de cima não é pythônica o suficiente. Para melhorar a legibilidade, fica da seguinte forma:
# print(nome[-1])

# No modo interativo do python é possível ver os índices através do comando:
# %indexes $nome

# Slicing - Fatiamento da sequência

# Da primeira até a quarta letra - Descrição de um intervalo que é fechado no início e aberto no final.
# Ou seja, o primeiro valor é inclusivo o primeiro termo e exclusivo para o segundo. Então a leitura
# pode ser feita do elemento 0 ATÉ o elemento 4.
# print(nome[0:4])

# O mesmo se aplica para os índices negativos.
# Do segundo, até o penúltimo.
# print(nome[1:-1])

# Com essa abordagem, todos aqueles métodos podem ser substituídos pelos slicing de strings.
# Assim, é possível imprimir até o último elemento da sequência através do seu comprimento:
# print(nome[0:len(nome)])

# Mas a string já sabe seu próprio comprimimento, então, não faz sentido calcular o comprimento da string novamente.
# De forma pythonica, teremos a omissão do último termo, já que a string sabe seu último elemento:
# print(nome[0:])

# Da mesma forma, o primeiro elemento a string também já conhece. De forma análoga a sequência sabe seu primeiro termo.
# Logo pode ser suprimido:
# print(nome[:4])

# Para imprimir todos elementos do primeiro até último, basta omitir o primeiro e último elemento do slicing:
# print(nome[:])

# Já para fazer o fateamento através de uma sequência definida, como por exemplo de 2 em 2 elementos,
# ou quantos se queira, # entra mais um novo parâmetro que é chamado de passo. Então, fica da seguinte forma:
# nome[primeiro_elemento_inclusico : segundo_elemento_exclusivo : passo ]. De dois em dois elementos fica,
# começando do elemento 1:
# print(nome[:: 2])
# A mesma coisa com índices negativos. Por exemplo, caso queira ver a lista de forma reversa:
# print(nome[::-1])

# Tal característica do Python é aplicada a qualquer sequência.
# Essa tecnologia somente é possível através de um conceito
# chamado em Python de Protocolo que utiliza a função built-in len().
# print(len)
# O len chama um método contido em strings chamado __len__()
# print(nome.__len__())
# Esse método é a implementação do len da sequência. Como se trata de um implementação mais baixo nível da linguagem.
# Recomenda-se utilizar a implementação mais alto nível, que no caso, é o len().
# O conceito de protocolo se torna mais evidente, quando é tentando acessar o atributo em tipos que não são sequências:
gravidade = 9.8
# print(gravidade.__len__())]
# O erro que aparecerá é -  print(gravidade.__len__())
#           ^^^^^^^^^^^^^^^^^
# AttributeError: 'float' object has no attribute '__len__'. Did you mean: '__le__'?
#
# Agora, se fizermos:
# len(gravidade)
# teremos outro erro. File "C:\Users\almei\github-repositorios\base_python\sequencias.py", line 69, in <module>
#     len(gravidade)
# TypeError: object of type 'float' has no len() - que é um erro de tipo que representa um erro muito mais específico.
# Em linhas gerais: O ponto flutuante não implementa o protocolo __len__()

# A anotação passando um índice de uma sequência, é um açucar sintático, ou seja,
# a implementação é traduzida para o método do protocolo implementado. Isso pode ser provado por:
# print(nome.__getitem__(0))

# Ou seja, a implementação anterior, é uma implementação bastante simplificada desta última. O mesmo açucar sintático
# ocorre no slicing.
indice = slice(1, -1, 2)

# o método faz normaliza os índices é justamente o método indices contidos nos slices.
# É possível verificar isso, através da linha abaixo:
# print(help(indice.indices))
# Assim, é possível com essa normalização fazer a conversão de índices negativos
# convertendo para o localização real da sequência
print(indice)
print(indice.indices(len(nome)))

# Outro açucar sintático
print(nome[indice])
print(nome.__getitem__(indice))