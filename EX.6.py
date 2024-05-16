def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    soma_pares = 0
    multiplicacao_impares = 1

    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            soma_pares += num
        else:
            multiplicacao_impares *= num

    print("A soma dos números pares é:", soma_pares)
    print("A multiplicação dos números ímpares é:", multiplicacao_impares)

if __name__ == "__main__":
    main()