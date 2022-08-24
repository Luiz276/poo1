#Este problema se resume em calcular qual dos pontos dados está mais próximo do ponto inicial, que é a bola branca
#Para calcular a distância, calcula-se a hipotenusa do triangulo formado pela bola branca e pela bola que se quer saber a distância, com a distância sendo a hipotenusa
#Logo após, compara-se as hipotenusas obtidas para descobrir qual o ponto mais próximo
resultados = []
c = int(input())
count = 0
while count<c:
    control = 28400.1
    nbolas = int(input())
    branca_x, branca_y = map(float, input().split())
    i = 0
    for x in range(0, nbolas):
        i += 1
        coordenadas_x, coordenadas_y = map(float, input().split())
        if branca_x>coordenadas_x:
            cateto1 = branca_x - coordenadas_x
        else:
            cateto1 = coordenadas_x - branca_x 
        if branca_y>coordenadas_y:
            cateto2 = branca_y - coordenadas_y
        else:
            cateto2 = coordenadas_y - branca_y
        hip = ((cateto1**2) + (cateto2**2))**(1/2)
        hip = hip * 10000
        hip = int(hip)
        hip = hip/10000
        if hip<control:
            control = hip
            win = i
    count += 1
    resultados.append(win)
print(*resultados, sep = "\n")