def main():
    numero = int(input("digite um numero: "))
    if numero % 2 == 0:
        print("é par")
    else:
        print("não é par")

def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

main()
