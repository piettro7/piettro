def calcular(primeiro, operador, segundo):

    
    if operador == "+":
        return primeiro + segundo
    elif operador == "-":
        return primeiro - segundo
    elif operador == "*":
        return primeiro * segundo
    elif operador == "/":
        if segundo != 0:
            return primeiro / segundo
        else:
            return "Erro, divisão por zero"
    else:
        return "Operador inválido"

def calculadora():

    entrada = input("Digite a operação no formato = numero operador numero: ")

    partes = entrada.split()

    if len(partes) == 3:

        primeiro = float(partes[0]) 
        operador = partes[1]    
        segundo = float(partes[2]) 
            
        resultado = calcular(primeiro, operador, segundo)

        print(f"Resultado: {resultado}")
    else:
        print("Digite no formato pedido")


calculadora()