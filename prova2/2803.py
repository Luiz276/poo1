#receber input do nome do estado e comparar com uma lista com os nomes dos estados da regiao norte. Caso ele esteja na regiao norte, printar "Regiao Norte"
s = str(input())
norte = "roraima acre amapa amazonas para rondonia tocantins"

if s in norte:
    print("Regiao Norte")
else:
    print("Outra regiao")