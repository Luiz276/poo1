import statistics

while True:
    try:
        #Importar a biblioteca statistics e usar mode
        #Mode retorna o valor mais comum
        num = list(map(int, input()))
        num.sort(reverse=True)
        print(statistics.mode(num))
        
    except EOFError:
        break