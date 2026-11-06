try: 
   num1 = int(input("Informe seu Primeiro Numero: "))
   num2 = int(input("Informe seu Segundo Numero: "))
   resultado = num1 + num2
   print("A Soma dos Valores Digitados Foram: ", resultado)
except ValueError:
   print("Campos Invalidos, Digite Novamente os (numeros Inteiros) ")