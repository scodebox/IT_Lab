def swap(l,i,j):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp

def partition(l,low,high):
    pivot = l[low]
    low+=1
    

# Main function.
if __name__ == '__main__':
    s =list("RANDOMIZATION")
    print (s)
    print (len(s))
    swap(s,0,12)
    print (s)