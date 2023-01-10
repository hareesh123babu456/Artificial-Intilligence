def addM(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(A[0])):
            result[i][j]=A[i][j] + B[i][j]

    for k in result:
        print(k)

    return 0
A=[ [4, 3, 3], [4, 3, 5], [1, 2, 8] ]

B=[ [5, 9, 2], [1, 7, 3], [6, 3, 0] ]

print("Result: ")
addM(A,B)
