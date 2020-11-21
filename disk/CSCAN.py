def schedule(req):
    seek_time=0
    current_pos=53
    l=[]
    r=[]
    for rq in req:
        if rq>current_pos:
            r.append(rq)
        else:
            l.append(rq)
    print("\nCurrent R/W position:",current_pos)
    if r:
        r.sort()
        for serving in r:
            print('Processing : REQ -> ',serving)
            seek_time+=abs(serving-current_pos)
            current_pos=serving
        if current_pos != 199:
            seek_time+=abs(199-current_pos)
            current_pos=199
    
    seek_time+=199
    current_pos=0
    if l:
        l.sort()
        for serving in l:
            print('Processing : REQ -> ',serving)
            seek_time+=abs(serving-current_pos)
            current_pos=serving

    return seek_time


if __name__ == '__main__':
    req = list(map(int,input('R/W REQ: ').split(' ')))
    # req = [98, 183, 37, 122, 14, 124, 65, 67]
    print('\nTotal seek time : ',schedule(req),'ms')