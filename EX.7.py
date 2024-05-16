numero = int(input("Digite um número inteiro e positivo: "))

if numero <= 0:
    print("O número deve ser inteiro e positivo.")
else:
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    print("O somatório de 1 até", numero, "é:", soma)
