def main():

    nota = int(input("qual a sua nota? (0 a 100) "))
    saber_nota(nota)


def saber_nota(nota):

    if nota > 100:
        print("nota de 0 a 100 por obsequio mano")
    elif nota >= 90 and nota <= 100:
        print("nota A")
    elif nota < 90 and nota >= 80:
        print("nota B")
    elif nota < 80 and nota >= 70:
        print("nota C")
    elif nota < 70 and nota >= 60:
        print("nota D")
    elif nota < 60 and nota >= 50:
        print("nota E")
    else:
        print("nota F, seu mediocre") 

main()