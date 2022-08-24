#Checar com ifs se as letras estão no restante que não foi distribuído
n = int(input())

for _ in range(n):
    resto = input()

    if 'Q' in resto:
        if 'J' in resto:
            if 'K' in resto:
                if 'A' in resto:
                    print("Aaah muleke")
                else:
                    print("Ooo raca viu")
            else:
                print("Ooo raca viu")
        else:
            print("Ooo raca viu")
    else:
        print("Ooo raca viu")