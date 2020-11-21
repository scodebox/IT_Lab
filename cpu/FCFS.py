def show_details(p_id,arrival_time,burst_time,completion_time):
    print("PID\tAT\tCPU\tCOM\tTAT\tWT")
    for i in range(0,len(p_id)):
        print (p_id[i],'\t',arrival_time[i],'\t',burst_time[i],'\t',completion_time[i],'\t',(completion_time[i]-arrival_time[i]),'\t',(completion_time[i]-arrival_time[i]-burst_time[i]))


def next_min_index(l,item):
    flag=1
    next_min=None
    index=None
    for i in range(0,len(l)):
        if l[i] > item and flag==1:
            next_min = l[i]
            flag=0
            index=i
        elif l[i]>item and l[i]<next_min and flag==0:
            next_min = l[i]
            index=i
    return index


def schedule(p_id,arrival_time,burst_time):
    completion_time = [0]*len(p_id)

    current_at_index = next_min_index(arrival_time,-1)
    current_time = arrival_time[current_at_index]

    # print (current_at_index)
    for i in p_id:
        if current_time < arrival_time[current_at_index]:
            current_time+=(arrival_time[current_at_index]-current_time)
        completion_time[current_at_index] = current_time + burst_time[current_at_index]
        current_time = completion_time[current_at_index]
        print ('Processing PID ',current_at_index)
        current_at_index = next_min_index(arrival_time, arrival_time[current_at_index])

    # print (completion_time)
    show_details(p_id,arrival_time,burst_time,completion_time)


if __name__ == '__main__':
    p_id = list(map(int,input('PROCESS IDs: ').split(' ')))
    arrival_time = list(map(int,input('ARRIVAL TIMEs: ').split(' ')))
    burst_time = list(map(int,input('BURST TIMEs: ').split(' ')))

    # p_id = [1, 2, 3, 4, 5]
    # arrival_time = [0, 1, 2, 3, 4]
    # burst_time = [2, 3, 6, 5, 4]

    # p_id = [1, 2, 3, 4, 5,6]
    # arrival_time = [6, 3, 5, 1, 4,2]
    # burst_time = [8, 3, 6, 2, 4,2]
    schedule(p_id,arrival_time,burst_time)
