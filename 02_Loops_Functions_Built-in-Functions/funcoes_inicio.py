# Diferentente de linguagens como Java que
# exitem formas de objeto se auto referenciar
# usando palavras reservadas como this,
# em python é necessário
# utilizar palavras especiais para esta referência.
# Elas são o __name__ e __file__ por exemplo.

print("Begin", __name__)
print("Início da primeira função:")


def primeira_funcao():
    print("Dentro da primeira função.")


# print("Chama a primeira_funcao.")
# primeira_funcao()

# Executando somente se este módulo for um entrypoint:
if __name__ == '__main__':
    print("Chama a primeira_funcao.")
    primeira_funcao()

print("End", __name__)

# Saída esperada inicial esperada:
# Begin __main__
# Início da primeira função:
# Foram da primeira_funcao.
# End __main__

# Begin __main__ -> nome do módulo - como primeiro.py é o entrypoint do programa,
# O python sobrescreve o nome do módulo para __main__
