def main():
    miaus = int(input("digite a quantidade de miaus: "))
    miar(miaus)

def miar(miaus):
    print("miauuuuu \n" * miaus , end = "")

def pegar_numero():

    while True:
        
        miaus = int(input("digite a quantidade de miaus: "))

        if miaus > 0:
            return miaus
        
main()