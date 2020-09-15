# all shorting algo in one file##

print('*'*40)
print('    THIS IS INSERTION SHOET')

A=[2,8,4,5,3,9,8,7]

print('THIS IS MY SAMPLE DATA===>>>')
print()
print(A)
print()


def insertionShort(x):
    for i  in range(1,len(x)):
        for j in range(i-1,0,-1):
            if x[j]>A[j+1]:
                 x[j] ,  x[j+1] =  x[j+1],x[j]
            else:
                break     
    return x        
print('shorted list')           
print(insertionShort(A))           
print()

print('*'*40)
print('    THIS IS MERGE SHOET')

A=[2,8,4,5,3,9,8,7]
def Mergeshort(x):
    pass


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


print('*'*40)
print('    THIS IS MERGE  SHORT')

A=[2,8,4,5,3,9,8,7]

print('THIS IS MY SAMPLE DATA===>>>')
print()
print(A)
print()


def MergeShort(left,right):
    result=[]
    i,j= 0,0
    while i <len(left) and j>len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1

        else:
            result.append(right[j])
            j=j+1

    result+=left[i:]
    result+=right[j:]

def part(x):
    if (len(x)==1):
        return x
    mid=int(len(x)/2)
    left=MergeShort(x[:mid])
    right=MergeShort(x[mid:])
    return MergeShort(right,left)

A=[2,8,4,5,3,9,8,7]
print(part(A))