def error_check(line1, line2):
    error_count=0
    error_index = []
    line1 = line1.strip()
    line2 = line2.strip()
    if len(line1) == len(line2):
        for i in range(0,len(line2)):
            if line1[i]!=line2[i]:
                error_count+=1
                error_index.append(i)
        print('Error index : ',error_index)
        print('Error count : ', error_count)
        print()
    else:
        print("Lengths are not matching. Maybe two line are completely different or spacing issue.")


file1 = open('file1.txt','r')
file2 = open('file2.txt','r')

line_number = 0

while True:
    line1 = file1.readline()
    line2 = file2.readline()
    if line1 == '' or line2 == '':
        break
    line_number+=1
    if line1 == line2:
        print("Line number ",line_number," MATCHED ")
    else:
        print("\nLine number ",line_number," ERROR")
        error_check(line1,line2)
    # print (1,line1.strip())
    # print (2,line2.strip())

file1.close()
file2.close()