# Function for removing task from the arrived job queue.
def remove(p_ids, arrival_time, burst_time, dlist):
    for id in dlist:
        index = p_ids.index(id)
        del p_ids[index]
        del arrival_time[index]
        del burst_time[index]

# Function for RR scheduling.


def schedule(p_ids, arrival_time, burst_time, completion_time):
    # Assuming time quantum is 2.
    TQ = 2
    # Job ready queue.
    job_queue = []
    t_burst = [0]*(len(p_ids)+1)
    flag = 0
    time = 0

    # Collecting arrived process in ready queue and deleting from the list.
    deleted_list = []
    for i in range(0, len(p_ids)):
        if arrival_time[i] <= time:
            job_queue.append(p_ids[i])
            t_burst[p_ids[i]] = burst_time[i]
            deleted_list.append(p_ids[i])
    remove(p_ids, arrival_time, burst_time, deleted_list)

    # Processing job in RR algorithm.
    while (len(p_ids) or max(t_burst)):
        # Collecting the arrived job when the flag is true.
        if flag:
            flag = 0
            deleted_list = []
            for i in range(0, len(p_ids)):
                if arrival_time[i] <= time:
                    job_queue.append(p_ids[i])
                    t_burst[p_ids[i]] = burst_time[i]
                    deleted_list.append(p_ids[i])
            remove(p_ids, arrival_time, burst_time, deleted_list)

        # If job available in job queue we start processing.
        if len(job_queue):
            # Takeing the process ID of first process from the job queue.
            PID = job_queue.pop(0)
            print('Processing PID ', PID)

            # When burst time of the job is more than the TQ.
            if t_burst[PID] > TQ:
                t_burst[PID] = t_burst[PID]-TQ
                time += TQ

                # Collecting arrived process in ready queue within the that TQ.
                deleted_list = []
                for i in range(0, len(p_ids)):
                    if arrival_time[i] <= time:
                        job_queue.append(p_ids[i])
                        t_burst[p_ids[i]] = burst_time[i]
                        deleted_list.append(p_ids[i])
                remove(p_ids, arrival_time, burst_time, deleted_list)

                # Adding the currect job in the end of the job queue.
                job_queue.append(PID)

            # If burst time is less than TQ.
            else:
                time += t_burst[PID]
                t_burst[PID] = 0

                # Savning the completion time of currect job that completed.
                completion_time[PID] = time

                # Setting the flag for collecting arrived process in ready queue.
                flag = 1
        else:
            # If no job is arrived till now.
            time += 1
            # setting flag for collecting job after idle time.
            flag = 1

#  Function for display details.


def show_details(p_id, arrival_time, burst_time, completion_time):
    print("PID\tAT\tCPU\tCOM\tTAT\tWT")
    # Printing all the details.
    for i in range(0, len(p_id)):
        print(p_id[i], '\t', arrival_time[i], '\t', burst_time[i], '\t', completion_time[p_id[i]], '\t',
              (completion_time[p_id[i]]-arrival_time[i]), '\t', (completion_time[p_id[i]]-arrival_time[i]-burst_time[i]))


# Main function.
if __name__ == '__main__':
    p_id = list(map(int, input('PROCESS IDs: ').split(' ')))
    arrival_time = list(map(int, input('ARRIVAL TIMEs: ').split(' ')))
    burst_time = list(map(int, input('BURST TIMEs: ').split(' ')))

    # p_id = [1, 2, 3, 4, 5, 6]
    # arrival_time = [0, 2, 3, 4, 5, 6]
    # burst_time = [4, 5, 2, 1, 6, 3]

    completion_time = [0]*(len(p_id)+1)
    # Calling the round robin scheduing function and passing the copy of details of the process.
    schedule(p_id[:], arrival_time[:], burst_time[:], completion_time)
    # Calling the display function for showing details.
    show_details(p_id, arrival_time, burst_time, completion_time)
