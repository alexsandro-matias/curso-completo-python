# Código replicado de primeiro.py
# print("Begin", __name__)
# print("Início da segunda função:")
#
#
# def segunda_funcao():
#     print("Dentro da segunda função.")
#
#
# print("Foram da segunda.")
#
# print("End", __name__)
# mesma saída do primeiro.py


print("Begin", __name__)
# Adicionando o módulo primeiro
import funcoes_inicio

print("Início da segunda função:")


def segunda_funcao():
    print("Dentro da segunda função.")
    funcoes_inicio.primeira_funcao()


print("Foram da segunda.")

print("End", __name__)

# saída alterada
# Begin __main__
# Begin primeiro
# Início da primeira função:
# Foram da primeira_funcao.
# End primeiro
# Início da segunda função:
# Foram da segunda.
# End __main__

# Isso acontece por que não apenas o import processa o arquivo,
# mas também executa todos as funções
# no corpo do módulo (funções globais).
# Somente no final da execução das funções é que retorna
# o controle da execução para o módulo testando_importe.py.
# Isso causa um efeito indesejado que é executar funções que não desejadas,
# ou seja, funções locais,
# já que somente as funções locais deveria ser invocadas no módulo segundo.
# Para evitar isso, basta no primeiro módulo e deixar um condicional para
# que somente se o módulo primeiro for o entrypoint
# o é que ele será executado como biblioteca.
