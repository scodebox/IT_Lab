# Function to search correct block for the process.
def find_index(blocks, proc):
    block_size = None
    # Searching for smalled block for the given process..
    for block in blocks:
        if proc <= block and block_size == None:
            block_size = block
        elif proc <= block and block < block_size:
            block_size = block

    # Block found for allocation.
    if block_size != None:
        return blocks.index(block_size)
    # Block not dounf for allocation.
    else:
        return -1


# Function implementing best fit.
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
    # Calling allocation for best fit.
    allocate(blocks, process)
