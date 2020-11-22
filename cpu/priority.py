def get_index(pid_q,at_q,pr_q):
    if pr_q.count(max(pr_q))>1:
        m=max(pr_q)
        min_l_at=[]
        min_l_pid=[]
        for i in range(0,len(pr_q)):
            if m == pr_q[i]:
                min_l_at.append(at_q[i])
                min_l_pid.append(pid_q[i])

        if min_l_at.count(min(min_l_at))>1:
            return min(min_l_pid)
        else:
            index = at_q.index(min(min_l_at))
            return pid_q[index]
        
    else:
        index = pr_q.index(max(pr_q)) 
        return pid_q[index]


def schedule(p_id,arrival_time,burst_time,priority,completion_time):    
    current_time=0

    while len(p_id):
        pid_q=[]
        at_q=[]
        pr_q=[]
        
        for i in range(0,len(p_id)):
            if arrival_time[i] <= current_time:
                pid_q.append(p_id[i])
                at_q.append(arrival_time[i])
                pr_q.append(priority[i])

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
            del priority[index]
        elif len(pid_q)>1:
            index = p_id.index(get_index(pid_q,at_q,pr_q))
            current_time+=burst_time[index]
            completion_time[p_id[index]]=current_time
            print ('Processing PID ',pid_q[index])
            del p_id[index]
            del arrival_time[index]
            del burst_time[index]
            del priority[index]
        else:
            current_time+=1
            

def show_details(p_id,priority,arrival_time,burst_time,completion_time):
    print("PID\tPRI\tAT\tCPU\tCOM\tTAT\tWT")
    for i in range(0,len(p_id)):
        print (p_id[i],'\t',priority[i],'\t',arrival_time[i],'\t',burst_time[i],'\t',completion_time[p_id[i]],'\t',(completion_time[p_id[i]]-arrival_time[i]),'\t',(completion_time[p_id[i]]-arrival_time[i]-burst_time[i]))



if __name__ == '__main__':
    p_id = list(map(int,input('PROCESS IDs: ').split(' ')))
    priority = list(map(int,input('PRIORITY: ').split(' ')))
    arrival_time = list(map(int,input('ARRIVAL TIMEs: ').split(' ')))
    burst_time = list(map(int,input('BURST TIMEs: ').split(' ')))

    # priority = [3, 2, 4, 6, 7]
    # p_id = [1, 2, 3, 4, 5]
    # arrival_time = [0, 1, 2, 3, 4]
    # burst_time = [2, 3, 6, 8, 9]

    completion_time = [0]*(len(p_id)+1)
    schedule(p_id[:],arrival_time[:],burst_time[:],priority[:],completion_time)
    # print (completion_time)
    show_details(p_id,priority,arrival_time,burst_time,completion_time)