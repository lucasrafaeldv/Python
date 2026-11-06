try:
    nota1 = float(input("Digite a Primeira nota do Aluno: "))
    nota2 = float(input("Digite a Segunda nota do Aluno: "))
    nota3 = float(input("Digite a Terceira nota do Aluno: "))
    media = (nota1+nota2+nota3)/3
    if media >= 6:
       print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")
except ValueError:
     print("Erro: Por favor, insira apenas números válidos para as notas.")