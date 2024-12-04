def main():
    x = float(input("digite um numero: "))
    y = float(input("digite mais um numero: "))
    verificando(x, y)

# definimos a função main

def verificando(x, y):
    if x < y:
        print(f"{x} é menor que {y}")
    elif x > y:
        print(f"{x} é maior que {y}")
    else:
        print(f"os numeros são iguais")

# definimos a função verificando

main()