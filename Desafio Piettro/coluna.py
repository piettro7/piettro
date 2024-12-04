def main():
    tamanho = int(input("coloque o tamanho da coluna: "))
    coluna(tamanho)

def coluna(tamanho):
    print("⬜\n" * tamanho, end = '')

main()