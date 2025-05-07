# Em outras linguagens como C/C++ e Java o escopo é delimitado pelas aspas.
# Em Python isso, não ocorre. Esta linguagem se baseia na identacao. Mas como o interpretador reconhece um escopo?
# Por que todo comando composto termina com ":" que funciona como delimitador de bloco.
#  A melhor forma de realizar esta identação é através 4 espaços

# Nível 0 da hierarquia
def qualquer():
    # Encontrou um comando composto passa para o nível 1
    # Esse reconhecimento é justamente pela diferença de identação.
    print('qualquer coisa ')
    # Mesmo nível já não se aumentou o número de espaços.
    print(9 * 8)
    # Então, a quantidade de espaços é indiferente, o que é necessário é que sejam o mesmo valor
    for i in range(10):
        # Hieraquia de Nível 2
        print(i)
    # Mas nesta abordagem, temos um problema, e se quisermos declarar um bloco de código vazio?
    # Existe uma palavra reservada para isso no Python - pass - ou seja ele não faz nada



# Linhas são consideradas de formas diferentes em Python, que são linhas físicas e linhas lógicas.
# No primeiro caso tudo que termina com o caracter de escape \n.
# Quando a linha tem um comando com um comprimento maior usa-se o símbolo da "\" para quebrar este comando em duas linhas.

if True and \
        True:
    print("Tudo verdadeiro")

# Porém essa abordagem peca na legibilidade.
# Para evitarmos isso, basta dar uma quebra de linha em comandos compostos que
# o Python ignora a identação por que percebe que se trata de uma continuação de um comando. como por exemplo na linha abaixo

print('Alexsandro ' +
      'Matias' +
      '.')
