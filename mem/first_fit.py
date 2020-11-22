def allocate(blocks,process):
	allocation_id = [1]*(len(process)+1)
	print("PID\tP_SIZ\tMEM_BLK\tREM_MEM")
	for i in range(0,len(process)):
		for j in range(0,len(blocks)):
			if blocks[j] >= process[i]:
				blocks[j] = blocks[j]-process[i]
				print (i,'\t',process[i],'\t',j,'\t',blocks[j])
				allocation_id[i]=0
				break

	for i in range(0,len(process)):
		if allocation_id[i]:
			print ('process ', i,' needs to wait.')



if __name__ == '__main__':
	blocks = [100, 500, 200, 300, 600]
	process = [212, 417, 112, 426]

	allocate(blocks,process)