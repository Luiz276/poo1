#Este problema se resume em calcular qual dos pontos dados está mais próximo do ponto inicial, que é a bola branca
#Para calcular a distância, calcula-se a hipotenusa do triangulo formado pela bola bola branca e pela bola que se quer saber a distância
#Logo após, compara-se as hipotenusas obtidas para descobrir qual o ponto mais próximo
c = int(input())
count = 0
control = 28400
while count<c:
    nbolas = int(input())
    branca_x, branca_y = map(float, input().split())
    i = 0
    for x in range(0, nbolas):
        i += 1
        coordenadas_x, coordenadas_y = map(float, input().split())
        if branca_x>=coordenadas_x:
            cateto1 = branca_x - coordenadas_x
        else:
            cateto1 = coordenadas_x - branca_x 
        if branca_y>=coordenadas_y:
            cateto2 = branca_y - coordenadas_y
        else:
            cateto2 = coordenadas_y - branca_y
        hip = (((cateto1)**2) + ((cateto2)**2))**(1/2)

        if hip<control:
            control = hip
            win = i
    count += 1
    print(f"{win}\n")
