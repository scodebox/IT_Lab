# Function to check current available resources can satisfy the demand of given process.
def check(avl, need):
	# If the available resources are more than the the demand return true else false.
	for i,j in zip(avl,need):
		if i<j:
			return False
	return True

# Function that checks system is in safe mode or not using bankers algorithm.
def check_safemode(max_need,current_allocation,total_available):
	remaining_need = []
	current_available=[0]*len(current_allocation[0])

	# Calculating the currently available resources.
	for i in current_allocation:
		current_available[0]+=i[0]
		current_available[1]+=i[1]
		current_available[2]+=i[2]
	for i in range(0,len(current_available)):
		current_available[i] = total_available[i]-current_available[i]

	# Calculating the remaining demand of the processes system need to satisfy.
	for i,j in zip(max_need, current_allocation):
		temp=[]
		for index in range(0,len(i)):
			temp.append(i[index]-j[index])
		remaining_need.append(temp)

	# Searching for safe sequence.
	track=[1]*len(current_allocation)
	status=True
	while status:
		status=False
		index=None
		# Checking remaining demands of all the processes.
		for process_id in range(0,len(remaining_need)):
			if track[process_id] and check(current_available,remaining_need[process_id]):
				status=True
				# Keeping track of all the process for avoid duplicate computation.
				track[process_id]=0
				# Add all the occupied resources to the currectly available resources after completion of the process.
				for u in range(0,len(current_available)):
					current_available[u]+=current_allocation[process_id][u]
				print ('Safe sequence :Process ',process_id)

	# If safe sequence is not found./Demand of some process has not matched.
	if max(track):
		print ('\nSystem is in unsafe state.')
	# Demand of some process has matched.
	else:
		print ('\nSystem is in safe state.')


# Main function.
if __name__ == '__main__':
	# All details of process needs and available system resources.
	max_need = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
	current_allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
	total_available = [10,5,7]
	# Calling for bankers algorithm for checking the system is in safe mode or not.
	check_safemode(max_need,current_allocation,total_available)