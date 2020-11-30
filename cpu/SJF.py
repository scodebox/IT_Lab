# Function for choosing the correct process from job queue for scheduling.
def get_index(pid_q, at_q, bt_q):
    # If there is more than one job having min burst time and have to look for min arrival / porcess ID.
    if bt_q.count(min(bt_q)) > 1:
        m = min(bt_q)
        min_l_at = []
        min_l_pid = []
        # Checking the least arrival time.
        for i in range(0, len(bt_q)):
            if m == bt_q[i]:
                min_l_at.append(at_q[i])
                min_l_pid.append(pid_q[i])

        # Returning the leaset arrival time.
        if min_l_at.count(min(min_l_at)) > 1:
            return min(min_l_pid)
        else:
            # Returning least process ID in case there is same arrival time.
            index = at_q.index(min(min_l_at))
            return pid_q[index]

    else:
        # Returning the min burst time.
        index = bt_q.index(min(bt_q))
        return pid_q[index]

# Function for SJF scheduling.


def schedule(p_id, arrival_time, burst_time, completion_time):
    current_time = 0

    # Processing the shortest job.
    while len(p_id):
        # Collecting all arrived process.
        pid_q = []
        at_q = []
        bt_q = []
        for i in range(0, len(p_id)):
            if arrival_time[i] <= current_time:
                pid_q.append(p_id[i])
                at_q.append(arrival_time[i])
                bt_q.append(burst_time[i])

        # If only one process is arrived, then we are processing that process.
        if len(pid_q) == 1:
            index = p_id.index(pid_q[0])
            current_time += burst_time[index]

            # Saving completion time.
            completion_time[p_id[index]] = current_time
            print('Processing PID ', pid_q[0])

            # Deleteing the process details from job queue when it is completed.
            del p_id[index]
            del arrival_time[index]
            del burst_time[index]

        # If more than one procees is arrived.
        elif len(pid_q) > 1:
            # Calling the get_index function for getting the correct process to schedule.
            index = p_id.index(get_index(pid_q, at_q, bt_q))
            current_time += burst_time[index]

            # Saving completion time.
            completion_time[p_id[index]] = current_time
            print('Processing PID ', pid_q[index])

            # Deleteing the process details from job queue when it is completed.
            del p_id[index]
            del arrival_time[index]
            del burst_time[index]
        else:
            # If no process has arrived till now.
            current_time += 1


#  Function for display details.
def show_details(p_id, arrival_time, burst_time, completion_time):
    print("PID\tAT\tCPU\tCOM\tTAT\tWT")
    # Printing all the details.
    for i in range(0, len(p_id)):
        print(p_id[i], '\t', arrival_time[i], '\t', burst_time[i], '\t', completion_time[p_id[i]], '\t',
              (completion_time[p_id[i]]-arrival_time[i]), '\t', (completion_time[p_id[i]]-arrival_time[i]-burst_time[i]))


# Main function.
if __name__ == '__main__':
    # p_id = list(map(int, input('PROCESS IDs: ').split(' ')))
    # arrival_time = list(map(int, input('ARRIVAL TIMEs: ').split(' ')))
    # burst_time = list(map(int, input('BURST TIMEs: ').split(' ')))

    p_id = [1, 2, 3, 4, 5]
    arrival_time = [0, 1, 2, 3, 4]
    burst_time = [7, 5, 6, 2, 4]
    completion_time = [0]*(len(p_id)+1)
    # Calling the SJF scheduing function and passing the copy of details of the process.
    schedule(p_id[:], arrival_time[:], burst_time[:], completion_time)
    # Calling the display function for showing details.
    show_details(p_id, arrival_time, burst_time, completion_time)
