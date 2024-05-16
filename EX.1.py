qntd = int(input("Quantas tabuadas você deseja calcular? "))

for _ in range(qntd):
    n = int(input("Digite o número da tabuada a ser calculada: "))
    limite = int(input("Digite até onde deseja multiplicar: "))

    print("Tabuada do", n, ":")
    for i in range(1, limite + 1):
        resultado = n * i
        print(n, "x", i, "=", resultado)
    print()
