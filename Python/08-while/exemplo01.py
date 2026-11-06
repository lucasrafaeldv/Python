senha = 0 

while senha != 1234:
    try:
        senha = int(input("Digite a Sua Senha: "))
    except:
        print("Valor invalido. Por Favor, Digite apenas numeros")

print("\nSenha Digitada com Sucesso")