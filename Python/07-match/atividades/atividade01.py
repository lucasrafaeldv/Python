try:
    num1 = float(input("Digite o Primeiro Numero: ").replace(",", "."))
except: 
    print("Valor Invalido Para Primeiro Numero")

try:    
    num2 = float(input("Digite o Segundo Numero: ").replace(",", "."))
except:
    print("Valor Invalido Para Segundo Numero")

try:        
    print("Digite uma das operações a seguir: \n")
    print("Para Multiplicação Digite *")
    print("Para Divisão Digite /")
    print("Para Subtração Digite -")
    print("Para Adição Digite +")
    operador = str(input("Digite a Operação Acima: "))
except:
    print("Operador Invalido")

match operador:
    case "*":
        resultado = num1 * num2
        print("O resultado deu: ", resultado)
    case "/":
        resultado = num1 / num2
        print("O resultado deu: ", resultado)
    case "-":
        resultado = num1 - num2
        print("O resultado deu: ", resultado)
    case "+":
        resultado = num1 + num2
        print("O resultado deu: ", resultado)
    case _:
        print('Operador Inválido')                    