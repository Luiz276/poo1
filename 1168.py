n = int(input())
for x in range(0, n):
    leds = 0
    numero = list(input())
    for y in range(0, len(numero)):
        numero[y] = int(numero[y])
        if numero[y] == (1):
            leds += 2
        elif numero[y] == (2):
            leds += 5
        elif numero[y] == (3):
            leds += 5
        elif numero[y] == (5):
            leds += 5
        elif numero[y] == (4):
            leds += 4
        elif numero[y] == (6):
            leds += 6
        elif numero[y] == (9):
            leds += 6
        elif numero[y] == (0):
            leds += 6
        elif numero[y] == (7):
            leds += 3
        elif numero[y] == (8):
            leds += 7
    print(f"{leds} leds")