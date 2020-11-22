# function for comparing char by char.
def error_check(line1, line2):
    error_count = 0   # var for counting errors.
    error_index = []    # list for keep recording error index.

    # striping out space or tab from start/end.
    line1 = line1.strip()
    line2 = line2.strip()

    # checking length of two lines.
    if len(line1) == len(line2):
        # char to char compare and record index & increase error count if mismatch found.
        for i in range(0, len(line2)):
            if line1[i] != line2[i]:
                error_count += 1
                error_index.append(i)
        print('Error index : ', error_index)
        print('Error count : ', error_count)
        print()
    else:
        print("Lengths are not matching. Maybe two line are completely different or spacing issue.")


# opening two files.
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

# line number counter.
line_number = 0

# loop for each lines in file.
while True:
    # reading one line from two files.
    line1 = file1.readline()
    line2 = file2.readline()

    # break the loop if it is end of the file.
    if line1 == '' or line2 == '':
        break

    # line count.
    line_number += 1

    # Checking lines are exactly same.
    if line1 == line2:
        print("Line number ", line_number, " MATCHED ")
    else:
        print("\nLine number ", line_number, " ERROR")
        # calling error check fucntion to compares char by char.
        error_check(line1, line2)
    # print (1,line1.strip())
    # print (2,line2.strip())

# closing those files.
file1.close()
file2.close()
