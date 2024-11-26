def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            fim = meio - 1
        else:
            inicio = meio + 1

    return None

# Exemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
resultado = busca_binaria(numeros, 7)

if resultado is not None:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")
