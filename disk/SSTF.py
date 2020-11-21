def search(req,current_pos):
    least_seek_time = abs(current_pos-req[0])
    index=0
    value=req[0]
    for i in range(0,len(req)):
        if abs(req[i]-current_pos)<least_seek_time:
            least_seek_time=abs(req[i]-current_pos)
            index=i
            value=req[i]

    # print('>>',index)
    # print('>>',value)
    req.pop(index)
    return value


def schedule(req):
    seek_time=0
    current_pos=53
    print("\nCurrent R/W position:",current_pos)
    while req:
        serving = search(req,current_pos)
        # print(current_pos,serving)
        print('Processing : REQ -> ',serving)
        seek_time+=abs(serving-current_pos)
        current_pos=serving

    return seek_time


if __name__ == '__main__':
    req = list(map(int,input('R/W REQ: ').split(' ')))
    # req = [98, 183, 37, 122, 14, 124, 65, 67]
    print('\nTotal seek time : ',schedule(req),'ms')
    