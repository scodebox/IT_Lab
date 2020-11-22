# Function for searching the closest request.
def search(req, current_pos):
    least_seek_time = abs(current_pos-req[0])
    index = 0
    value = req[0]

    # Searching.
    for i in range(0, len(req)):
        if abs(req[i]-current_pos) < least_seek_time:
            least_seek_time = abs(req[i]-current_pos)
            index = i
            value = req[i]
    req.pop(index)
    return value

# Function implements the SSTF algorithm.


def schedule(req):
    seek_time = 0
    # Assuming the current head position is 53.
    current_pos = 53
    print("\nCurrent R/W position:", current_pos)

    # Serving the request nearest position.
    while req:
        # getting the nearest position.
        serving = search(req, current_pos)
        print('Processing : REQ -> ', serving)
        # computing the seek time.
        seek_time += abs(serving-current_pos)
        current_pos = serving

    # Returing the total seek time.
    return seek_time


# Main function.
if __name__ == '__main__':
    req = list(map(int, input('R/W REQ: ').split(' ')))
    # req = [98, 183, 37, 122, 14, 124, 65, 67]
    # Calling seheduling for SCAN.
    print('\nTotal seek time : ', schedule(req), 'ms')
