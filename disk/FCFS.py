# Function implements the FCFS algorithm.
def schedule(req):
    seek_time = 0
    current_pos = 0
    print("\nCurrent R/W position:", current_pos)

    # Serving all the request FCFS manner.
    while req:
        serving = req.pop(0)
        print('Processing : REQ -> ', serving)
        # Calculating the seek time.
        seek_time += abs(serving-current_pos)
        current_pos = serving

    # Returing the total seek time.
    return seek_time


# Main function.
if __name__ == '__main__':
    # req = list(map(int,input('R/W REQ: ').split(' ')))
    req = [98, 183, 37, 122, 14, 124, 65, 67]
    # Calling seheduling for FCFS.
    print('\nTotal seek time : ', schedule(req), 'ms')
