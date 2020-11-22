# Function implementing next fit.
def allocate(blocks, process):
    allocation_id = [1]*(len(process)+1)
    print("PID\tP_SIZ\tMEM_BLK\tREM_MEM")

    # Allocating the memory to the process.
    index = 0
    for i in range(0, len(process)):
        count = 0
        while count < len(blocks):
            if blocks[index] >= process[i]:
                blocks[index] = blocks[index]-process[i]
                print(i, '\t', process[i], '\t', index, '\t', blocks[index])
                allocation_id[i] = 0
                break
            count += 1
            index = (index+1) % len(blocks)

    # Memory not allocated.
    for i in range(0, len(process)):
        if allocation_id[i]:
            print('process ', i, ' needs to wait.')


# Main function.
if __name__ == '__main__':
    blocks = [100, 500, 200, 300, 600]
    process = [212, 417, 112, 426]
    # Calling allocation for best fit.
    allocate(blocks, process)
