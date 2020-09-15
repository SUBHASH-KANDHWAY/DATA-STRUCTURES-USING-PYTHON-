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