def merge(l,start,mid,end):
    i = start
    j = mid+1
    temp = []
    temp_index=0
    
    while i<= mid and j<=end:
        if l[i] <= l[j]:
            temp.append(l[i])
            i+=1
        if l[i] > l[j]:
            temp.append(l[j])
            j+=1

    if i>mid:
        while j<=end:
            temp.append(l[j])
            j+=1
    
    if j>end:
        while i<=mid:
            temp.append(l[i])
            i+=1

    for x in range(start,end+1):
        l[x]=temp[temp_index]
        temp_index+=1



def divide(l,start,end):
    if start>=end:
        return

    mid = int((start+end)/2)
    divide(l,start,mid)
    divide(l,mid+1,end)
    merge(l,start,mid,end)
    

if __name__ == '__main__':
    l = [3, 41, 52, 26, 38, 57, 9, 49]
    print('INPUT : ',l)
    divide(l,0,len(l)-1)
    print ('SORTED :',l)