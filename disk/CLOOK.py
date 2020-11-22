# Function implements the CLOOK algorithm.
def schedule(req):
    seek_time = 0
    # Assuming the current head position is 53 and moving towards higher track.
    current_pos = 53
    l = []
    r = []
    print("\nCurrent R/W position:", current_pos)

    # Collecting all the requests can be served in the path.
    for rq in req:
        if rq > current_pos:
            r.append(rq)
        else:
            l.append(rq)

    # Serving the request in the path.
    if r:
        r.sort()
        for serving in r:
            print('Processing : REQ -> ', serving)
            seek_time += abs(serving-current_pos)
            current_pos = serving

    # Moving bank to the lowest requested track.
    seek_time += abs(max(r)-min(l))
    current_pos = min(l)

    # Serving all the request towards moving higher track.
    if l:
        l.sort()
        for serving in l:
            print('Processing : REQ -> ', serving)
            seek_time += abs(serving-current_pos)
            current_pos = serving

    # Returing the total seek time.
    return seek_time


# Main function.
if __name__ == '__main__':
    req = list(map(int, input('R/W REQ: ').split(' ')))
    # req = [98, 183, 37, 122, 14, 124, 65, 67]
    # Calling seheduling for CLOOk.
    print('\nTotal seek time : ', schedule(req), 'ms')
