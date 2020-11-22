# Function for searching the biggest block.
def find_index(blocks, proc):
    max_block = max(blocks)
    if max_block >= proc:
        return blocks.index(max_block)
    # If the biggest block can not hold the process then return -1.
    else:
        return -1


# Function implementing worst fit.
def allocate(blocks, process):
    allocation_id = [1]*(len(process)+1)
    print("PID\tP_SIZ\tMEM_BLK\tREM_MEM")

    # Allocating the memory to the process.
    for i in range(0, len(process)):
        # Getting the correct memory block.
        index = find_index(blocks, process[i])
        # If block found for the allocation.
        if index != -1:
            # Updating the block size after allocation of a process.
            blocks[index] = blocks[index]-process[i]
            print(i, '\t', process[i], '\t', index, '\t', blocks[index])
            allocation_id[i] = 0

    # Memory not allocated.
    for i in range(0, len(process)):
        if allocation_id[i]:
            print('process ', i, ' needs to wait.')


# Main function.
if __name__ == '__main__':
    blocks = [100, 500, 200, 300, 600]
    process = [212, 417, 112, 426]
    # Calling allocation for worst fit.
    allocate(blocks, process)
