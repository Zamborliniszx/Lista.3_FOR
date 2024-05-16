opt = input(" Digite C para CRESCENTE ou D para DECRESCENTE: ")

if opt.upper() == "C":
    for i in range(1,101):
        if i % 3 == 0:
            print(i)

elif opt.upper() == "D":
    for i in range(100, 0, -1):
        if i % 3 == 0:
            print(i)