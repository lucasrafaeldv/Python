try: 
    nomeAluno = str(input("Digite aqui Seu nome de aluno: "))
    idade = int(input("Digite sua Idade: "))
    print("Ola seja Bem vindo!", nomeAluno)
except ValueError:
    print("Erro: Verifique seu Login e tente novamente.")
    