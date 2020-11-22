def find_index(blocks,proc):
	block_size=None
	for block in blocks:
		if proc <= block and block_size == None:
			block_size=block
		elif proc <= block and block <block_size:
			block_size=block

	if block_size != None:
		return blocks.index(block_size)
	else:
		return -1



def allocate(blocks,process):
	allocation_id = [1]*(len(process)+1)
	print("PID\tP_SIZ\tMEM_BLK\tREM_MEM")
	for i in range(0,len(process)):
		index = find_index(blocks,process[i])
		if index!=-1:
			blocks[index] = blocks[index]-process[i]
			print (i,'\t',process[i],'\t',index,'\t',blocks[index])
			allocation_id[i]=0

	for i in range(0,len(process)):
		if allocation_id[i]:
			print ('process ', i,' needs to wait.')


if __name__ == '__main__':
	blocks = [100, 500, 200, 300, 600]
	process = [212, 417, 112, 426]

	allocate(blocks,process)