n, m = map(int, input().split())
while n != 0:
    mat = []

    solvedAll = 1 #one team solved all problems
    least1person = 1 #every problem was solved at least once
    everyoneSolved = 1 #no problem was solved by everyone
    least1problem =1 #everyone solved at least one problem

    countSolved = 0
    countLeast1person = 0

    for x in range(n):
        mat.append(list(map(int, input().strip().split())))
        #Checking if somebody solved all problems
        if min(mat[x]) == 1:
            solvedAll = 0
            #print("Solved all")
        #Checking if somebody didn't solve any problems
        if max(mat[x]) == 0:
            least1problem = 0
            #print("At least 1 problem")

    for y in range(m):
        countSolved = 0
        for x in range(n):
            #checking if at least one problem was solved by everyone
            if mat[x][y] != 0:
                countSolved += 1
            if countSolved == n:
                everyoneSolved = 0
                #print("a problem was solved by everyone")
            elif countSolved == 0 and x == n-1:
                countLeast1person += 1

    #checking if a problem was not solved by at least one team        
    if countLeast1person >0:
        least1person = 0
        #print("a problem wasn't solved")

    print(solvedAll + least1problem + everyoneSolved + least1person)

    n, m = map(int, input().split())