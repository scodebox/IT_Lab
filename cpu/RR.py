def remove(p_ids,arrival_time,burst_time,dlist):
    for id in dlist:
        index = p_ids.index(id)
        del p_ids[index]
        del arrival_time[index]
        del burst_time[index]


def schedule(p_ids,arrival_time,burst_time,completion_time):
    TQ=2
    job_queue=[]
    t_burst=[0]*(len(p_ids)+1)
    flag = 0
    time = 0

    deleted_list=[]
    for i in range(0,len(p_ids)):
        if arrival_time[i] <= time:
            job_queue.append(p_ids[i])
            t_burst[p_ids[i]] = burst_time[i]
            deleted_list.append(p_ids[i])
    remove(p_ids,arrival_time,burst_time,deleted_list)

    while (len(p_ids) or max(t_burst)):
        if flag:
            flag=0
            deleted_list=[]
            for i in range(0,len(p_ids)):
                if arrival_time[i] <= time:
                    job_queue.append(p_ids[i])
                    t_burst[p_ids[i]] = burst_time[i]
                    deleted_list.append(p_ids[i])
            remove(p_ids,arrival_time,burst_time,deleted_list)

        if len(job_queue):
            PID = job_queue.pop(0)
            print ('Processing PID ',PID)
            if t_burst[PID] > TQ:
                t_burst[PID]=t_burst[PID]-TQ
                time+=TQ

                deleted_list=[]
                for i in range(0,len(p_ids)):
                    if arrival_time[i] <= time:
                        job_queue.append(p_ids[i])
                        t_burst[p_ids[i]] = burst_time[i]
                        deleted_list.append(p_ids[i])
                remove(p_ids,arrival_time,burst_time,deleted_list)

                job_queue.append(PID)
            else:
                time+=t_burst[PID]
                t_burst[PID]=0
                completion_time[PID] = time
                flag=1
        else:
            time+=1
            flag=1


def show_details(p_id,arrival_time,burst_time,completion_time):
    print("PID\tAT\tCPU\tCOM\tTAT\tWT")
    for i in range(0,len(p_id)):
        print (p_id[i],'\t',arrival_time[i],'\t',burst_time[i],'\t',completion_time[p_id[i]],'\t',(completion_time[p_id[i]]-arrival_time[i]),'\t',(completion_time[p_id[i]]-arrival_time[i]-burst_time[i]))
        


if __name__ == '__main__':
    p_id = list(map(int,input('PROCESS IDs: ').split(' ')))
    arrival_time = list(map(int,input('ARRIVAL TIMEs: ').split(' ')))
    burst_time = list(map(int,input('BURST TIMEs: ').split(' ')))

    # p_id = [1, 2, 3, 4, 5, 6]
    # arrival_time = [0, 2, 3, 4, 5, 6]
    # burst_time = [4, 5, 2, 1, 6, 3]

    completion_time = [0]*(len(p_id)+1)
    schedule(p_id[:],arrival_time[:],burst_time[:],completion_time)
    # print (completion_time)
    show_details(p_id,arrival_time,burst_time,completion_time)
