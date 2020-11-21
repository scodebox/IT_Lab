def max_heapify(a,index):
    next_level = (2*index)
    item = a[index]
    
    while next_level<=len(a)-1:
        if next_level<(len(a)-1) and a[next_level]<a[next_level+1]:
            next_level+=1
        if a[next_level] <= item:
            break
        a[int(next_level/2)] = a[next_level]
        next_level=next_level*2

    a[int(next_level/2)] = item


def build_heap(a):
    for index in range(int(len(a)/2),0,-1):
        max_heapify(a,index)


def extract_max_heap(a):
    max_element = a[1]
    a[1] = a[-1]
    del a[-1]
    if len(a)>1:
        max_heapify(a,1)
    return max_element


if __name__ == '__main__':
    a = [None, 8, 13, 9, 5, 12, 15, 7, 4, 0, 6, 2, 1]
    print ('INPUT:',a[1:])
    build_heap(a)
    print ('HEAP:',a[1:])

    op = [0]*(len(a)-1)
    for i in range((len(a)-2),-1,-1):
        op[i] = extract_max_heap(a)
    print ('SORTED:',op)