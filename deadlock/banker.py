def check(avl, need):
	for i,j in zip(avl,need):
		if i<j:
			return False
	return True


def check_safemode(max_need,current_allocation,total_available):
	remaining_need = []
	current_available=[0]*len(current_allocation[0])
	for i in current_allocation:
		current_available[0]+=i[0]
		current_available[1]+=i[1]
		current_available[2]+=i[2]
	for i in range(0,len(current_available)):
		current_available[i] = total_available[i]-current_available[i]

	for i,j in zip(max_need, current_allocation):
		temp=[]
		for index in range(0,len(i)):
			temp.append(i[index]-j[index])
		remaining_need.append(temp)

	# print (remaining_need)
	# print (current_available)
	# print (current_allocation)
	track=[1]*len(current_allocation)
	status=True
	while status:
		status=False
		index=None
		for process_id in range(0,len(remaining_need)):
			if track[process_id] and check(current_available,remaining_need[process_id]):
				status=True
				track[process_id]=0
				# print (current_available)
				# print (remaining_need[index])
				# print (current_allocation[index])
				for u in range(0,len(current_available)):
					current_available[u]+=current_allocation[process_id][u]
				# print (current_available)
				print ('Safe sequence :Process ',process_id)

	if max(track):
		print ('\nSystem is in unsafe state.')
	else:
		print ('\nSystem is in safe state.')



if __name__ == '__main__':
	max_need = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
	current_allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
	total_available = [10,5,7]

	# print (max_need)
	# print (current_allocation)
	# print (total_available)
	check_safemode(max_need,current_allocation,total_available)