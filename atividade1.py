numero = None

while numero is None:
    try:
        numero = int(input("Digite um numero: "))
    except ValueError:
        print("Erro! Digite apenas números inteiros.")

print(f"Número: {numero}")
