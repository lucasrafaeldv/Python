print("1 - Domingo")
print("2 - Segunda-Feira")
print("3 - Terça-Feira")
print("4 - Quarta-Feira")
print("5 - Quinta-Feira")
print("6 - Sexta-Feira")
print("7 - Sábado")

try: 
    diaSemana = int(input("Digite o número correspondente ao dia acima: "))

    match diaSemana:
        case 1: 
            print("Seu dia da semana é Domingo")
        case 2:
            print("Seu dia da semana é Segunda-Feira")
        case 3:
            print("Seu dia da semana é Terça-Feira")  
        case 4:
            print("Seu dia da semana é Quarta-Feira")
        case 5:
            print("Seu dia da semana é Quinta-Feira")
        case 6:
            print("Seu dia da semana é Sexta-Feira")
        case 7:
            print("Seu dia da semana é Sábado")
        case _:
            print("Número informado inválido! Escolha de 1 a 7.")

except ValueError:
    print("Valor inválido! Por favor, digite apenas números inteiros de 1 a 7.")