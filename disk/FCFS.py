def schedule(req):
    seek_time=0
    current_pos=0
    print("\nCurrent R/W position:",current_pos)
    while req:
        serving = req.pop(0)
        # print(current_pos,serving)
        print('Processing : REQ -> ',serving)
        seek_time+=abs(serving-current_pos)
        current_pos=serving

    return seek_time


if __name__ == '__main__':
    req = list(map(int,input('R/W REQ: ').split(' ')))
    # req = [98, 183, 37, 122, 14, 124, 65, 67]
    print('\nTotal seek time : ',schedule(req),'ms')
    