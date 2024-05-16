n = int(input("Digite um número inteiro e positivo (n): "))

if n <= 0:
    print("O número deve ser inteiro e positivo.")
else:
    harmonico = 0
    for i in range(1, n + 1):
        harmonico += 1 / i

    print("O valor de H(",n,") é:", harmonico)