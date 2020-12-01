# Function for element swap.
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


# Function for the partiton.
def partition(l, start, end):
    pivot = l[end]
    rev = start-1
    for index in range(start, end):
        if l[index] <= pivot:
            rev += 1
            swap(l, rev, index)
    swap(l, rev+1, end)
    return rev+1


# Function for quick sort.
def quick_sort(l, start, end):
    if start < end:
        p = partition(l, start, end)
        quick_sort(l, start, p-1)
        quick_sort(l, p+1, end)


# Main function.
if __name__ == '__main__':
    s = "RANDOMIZATION"
    print('INPUT : ', s)
    s = list(s)
    quick_sort(s, 0, len(s)-1)
    print('SORTED : ', ''.join(s))
