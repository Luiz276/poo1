while True:
    try:
        resultado_h = []
        resultado_m = []
        h, m = map(int, input().split(":"))
        bin_h = list(bin(h))
        bin_m = list(bin(m))
        
        del bin_h[0]
        del bin_h[0]

        del bin_m[0]
        del bin_m[0]

        if len(bin_h) < 4:
            for x in range(len(bin_h), 4):
                bin_h.insert(0, 0)
        if len(bin_m) < 6:
            for x in range(len(bin_m), 6):
                bin_m.insert(0,0)
                
        for x in range(len(bin_h)):
            if (bin_h[x] == 0) or (bin_h[x] == '0'):
                resultado_h.append(" ")
            else:
                resultado_h.append("o")

        for x in range(len(bin_m)):
            if (bin_m[x] == 0) or (bin_m[x] == '0'):
                resultado_m.append(" ")
            else:
                resultado_m.append("o")
        
        print(f""" ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |
|   |  """, end = " ")

        print(*resultado_h, sep = "         ", end = " ")

        print(""" |   |
|   |                                    |   |
|   |                                    |   |
|   |  """, end = " ")
        print(*resultado_m, sep = "     ", end = " ")
        print(""" |   |
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|""")
        print("")

    except EOFError:
        break