num = -1

while num < 0:
    num = int(input("Digite um número positivo: "))
    if num < 0:
        print("ERRO! O número deve ser positivo.")

print(f"Número: {num}")
