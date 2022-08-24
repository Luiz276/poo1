n = int(input())
resultados = []
while n!= 0:
    resultados = []
    for x in range(0,n):
        alternativas = input().split()
        alternativas[0] = int(alternativas[0])
        alternativas[1] = int(alternativas[1])
        alternativas[2] = int(alternativas[2])
        alternativas[3] = int(alternativas[3])
        alternativas[4] = int(alternativas[4])
        for i in range(0,5):
            if alternativas[i] <= 127:
                resultados.append(i)
        if len(resultados) !=1:
            print("*")
        elif resultados[0] == 0:
            print("A")
        elif resultados[0] == 1:
            print("B")
        elif resultados[0] == 2:
            print("C")
        elif resultados[0] == 3:
            print("D")
        elif resultados[0] == 4:
            print("E")
        resultados = []
    n = int(input())