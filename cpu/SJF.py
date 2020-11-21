if __name__ == '__main__':
    # p_id = list(map(int,input('PROCESS IDs: ').split(' ')))
    # arrival_time = list(map(int,input('ARRIVAL TIMEs: ').split(' ')))
    # burst_time = list(map(int,input('BURST TIMEs: ').split(' ')))

    p_id = [1, 2, 3, 4, 5]
    arrival_time = [0, 1, 2, 3, 4]
    burst_time = [7, 5, 6, 2, 4]

    # p_id = [1, 2, 3, 4, 5,6]
    # arrival_time = [6, 3, 5, 1, 4,2]
    # burst_time = [8, 3, 6, 2, 4,2]
    schedule(p_id,arrival_time,burst_time)