print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")



try:

    valInicial = float(1.000,00), input(print("Digite a Interação Bancaria Desejada."))
    match valInicial:
        case 1:
            print("Seu Saldo e de: ", valInicial)
        case 2:    
            input(print("Digite o Valor que Deseja Depositar: "))
        case 3:    
            input(print("Digite o Valor que Deseja Sacar: "))
        case 4:
            print("Você saiu da Interface Bancaria Correspondente")       
except:
    print("Interação Invalida, Digite o Numero Referente a Ação Desejada.")