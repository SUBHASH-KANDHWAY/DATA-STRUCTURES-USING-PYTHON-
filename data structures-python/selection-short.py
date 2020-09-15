
print('*'*40)
print('    THIS IS SELECTION  SHORT')

A=[2,8,4,5,3,9,8,7]

print('THIS IS MY SAMPLE DATA===>>>')
print()
print(A)
print()


def SelectionShort(x):
    indexOfLength=range(0, len(x)-1)

    for i in indexOfLength:
        minvalue=1

        for j in range(i+1  , len(x)):
            if x[j]< x[minvalue]:
                minvalue=j
        if minvalue!=i:
                 x[i] ,x[minvalue]= x[minvalue] , x[i]  

    return x

print(SelectionShort(A))

