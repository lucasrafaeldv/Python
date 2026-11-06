try: 
    precoProd = float(input("Digite o Preco do Produto Disponivel: "))
    percentuaDesc = float(input("Aplique aqui o Desconto Percentual: "))
    valorDesconto = precoProd * (percentuaDesc / 100)
    precoFinal = precoProd - valorDesconto

    print("O seu Preço final do Produto Disponivel, Foi de:  ", precoFinal, "RS")
except ValueError:
    print("Valores Foram Informados Errados, por favor Digitr novamente. ")