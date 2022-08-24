#usar .replace() para trocar " ," e " ." po "," e ".", respectivamente
while True:
    try:
        entrada = str(input())
        x = entrada.replace(" ,", ',')
        y = x.replace(" .", ".")
        print(y)
    except EOFError:
        break