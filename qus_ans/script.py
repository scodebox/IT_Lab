import os


# Function to extract question number from file name.
def get_qus_number(file_name):
    return file_name[8:-4]


# Function to generate the answer file name from question file name.
def generate_ans_filename(file_name):
    return ('answer'+file_name[8:])


# Funcion to merger both files.
def merge_files(qus_files, ans_files):
    for qus_file_name in qus_files:
        # Getting the question number.
        qus_number = get_qus_number(qus_file_name)
        # Getting the answer file name.
        ans_file_name = generate_ans_filename(qus_file_name)

        # Reading the question from file.
        question = open(qus_file_name, 'r').read()
        new_file_name = 'merge'+qus_number+'.txt'

        print(" MERGING : ", qus_file_name)

        # When answer file exist.
        if ans_file_name in ans_files:
            # Reading the answer file.
            answer = open(ans_file_name, 'r').read()

            # Create new file.
            new_file = open(new_file_name, 'w')

            # Writing into the file.
            new_file.write(str("QUESTION \n"))
            new_file.write(str(question))
            new_file.write(str('\n'))
            new_file.write(str("ANSWER : \n"))
            new_file.write(str(answer))

            # Closing the file.
            new_file.close()
        else:
            # When answer file doesn't exist.
            # Create new file.
            new_file = open(new_file_name, 'w')

            # Writing into the file.
            new_file.write(str("QUESTION \n"))
            new_file.write(str(question))
            new_file.write(str('\n'))
            new_file.write(str("ANSWER : \n"))
            new_file.write(str("\tNOT FOUND!"))

            # Closing the file.
            new_file.close()


# Function for separating question and answer files.
def separate_file_names(list_of_files):
    # List for storing answer file name.
    ans_files = []
    # List for storing question file name.
    qus_files = []

    print(" PROCESSING...")

    # Separating file by name.
    for file_name in list_of_files:
        if len(file_name) > 6:

            if str.lower(file_name[0:6]) == 'answer':
                # Adding answer file to the list.
                ans_files.append(file_name)

            elif str.lower(file_name[0:8]) == 'question':
                # Adding question file to the list.
                qus_files.append(file_name)

    # Returning two list.
    return qus_files, ans_files


if __name__ == '__main__':
    # collecting list of files from current directory.
    list_of_files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # separating question and answer files.
    qus_files, ans_files = separate_file_names(list_of_files)
    # Merging into one file.
    merge_files(qus_files, ans_files)
