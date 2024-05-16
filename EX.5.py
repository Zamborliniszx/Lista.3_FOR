soma = 0

for i in range(10):
    valor = float(input("Digite o {}º valor: ".format(i + 1)))
    soma += valor

media = soma / 10

print("A soma dos valores digitados é:", soma)
print("A média dos valores digitados é:", media)