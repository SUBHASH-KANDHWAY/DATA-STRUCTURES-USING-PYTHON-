
print('*'*40)
print('    THIS IS Quick SHOET')

A=[2,8,4,5,3,9,8,7]
def QuickShort(x):
    length=len(x)
    if length <=1:
        return x
    else:
        pivot=x.pop()

    bigger=[]
    lower=[]


    for i in x:
        if i>pivot:
            bigger.append(i)

        else:
            lower.append(i)

    return QuickShort(lower)+[pivot]+QuickShort(bigger)
print(QuickShort(A))


    
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
print(QuickShort(A))

print(SelectionShort(A))