def get_index(pid_q,at_q,bt_q):
    if bt_q.count(min(bt_q))>1:
        m=min(bt_q)
        min_l_at=[]
        min_l_pid=[]
        for i in range(0,len(bt_q)):
            if m == bt_q[i]:
                min_l_at.append(at_q[i])
                min_l_pid.append(pid_q[i])

        if min_l_at.count(min(min_l_at))>1:
            return min(min_l_pid)
        else:
            index = at_q.index(min(min_l_at))
            return pid_q[index]
        
    else:
        index = bt_q.index(min(bt_q)) 
        return pid_q[index]


def schedule(p_id,arrival_time,burst_time,completion_time):
    # print (p_id)
    # print (arrival_time)
    # print (burst_time)
    
    current_time=0
    

    while len(p_id):
        pid_q=[]
        at_q=[]
        bt_q=[]
        
        for i in range(0,len(p_id)):
            if arrival_time[i] <= current_time:
                pid_q.append(p_id[i])
                at_q.append(arrival_time[i])
                bt_q.append(burst_time[i])

        # print(pid_q)
        # print(at_q)
        # print(bt_q)

        if len(pid_q)==1:
            index = p_id.index(pid_q[0])
            current_time+=burst_time[index]
            completion_time[p_id[index]]=current_time
            print ('Processing PID ',pid_q[0])
            del p_id[index]
            del arrival_time[index]
            del burst_time[index]
        elif len(pid_q)>1:
            index = p_id.index(get_index(pid_q,at_q,bt_q))
            current_time+=burst_time[index]
            completion_time[p_id[index]]=current_time
            print ('Processing PID ',pid_q[index])
            del p_id[index]
            del arrival_time[index]
            del burst_time[index]
        else:
            current_time+=1

        # print (completion_time)
        # print (p_id)
        # print (arrival_time)
        # print (burst_time)


def show_details(p_id,arrival_time,burst_time,completion_time):
    print("PID\tAT\tCPU\tCOM\tTAT\tWT")
    for i in range(0,len(p_id)):
        print (p_id[i],'\t',arrival_time[i],'\t',burst_time[i],'\t',completion_time[p_id[i]],'\t',(completion_time[p_id[i]]-arrival_time[i]),'\t',(completion_time[p_id[i]]-arrival_time[i]-burst_time[i]))
        


if __name__ == '__main__':
    p_id = list(map(int,input('PROCESS IDs: ').split(' ')))
    arrival_time = list(map(int,input('ARRIVAL TIMEs: ').split(' ')))
    burst_time = list(map(int,input('BURST TIMEs: ').split(' ')))

    # p_id = [1, 2, 3, 4, 5]
    # arrival_time = [0, 1, 2, 3, 4]
    # burst_time = [7, 5, 6, 2, 4]

    # p_id = [1, 2, 3, 4, 5,6]
    # arrival_time = [6, 3, 5, 1, 4,2]
    # burst_time = [8, 3, 6, 2, 4,2]
    completion_time = [0]*(len(p_id)+1)
    schedule(p_id[:],arrival_time[:],burst_time[:],completion_time)
    show_details(p_id,arrival_time,burst_time,completion_time)
