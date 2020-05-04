# File: Assignment_8_1.py
# Name:  Deborah Hunton
# Due Date: 5/3/20
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do following:
# Process the file: Gettysburg.txt
# Calculate the total words
# Output the number of occurrences of each word in the file
#
# This will include four functions:
#    add_word to add words to the dictionary (parameters: word, dictionary), no return
#    process_line to strip out bad characters, split out words and call add_word (parameters: line, dictionary),
#         no return
#    pretty_print to format the dictionary and print to the screen cleanly (parameters: dictionary), no return
#    main to read in the file, call process_line for each line, and call pretty_print when all lines processed

def add_word(word, my_dictionary):
    my_word = word.lower()
    if my_word not in my_dictionary:
        my_dictionary[my_word] = 1
    else:
        my_dictionary[my_word] += 1

def process_line(line, my_dictionary):
    my_line = line.strip()
    my_line = my_line.translate(str.maketrans('', '', string.punctuation))
    words = my_line.split()
    for word in words:
        add_word(word, my_dictionary)

def pretty_print(my_dictionary):
    message = f'There are {len(my_dictionary)} words in the file.'
    print(message)

    header = '{0:^15}{1:^8}'.format('Word','#')
    header_sep = '{0:^15}{0:^8}'.format('--------')
    pretty = list()
    for key, val in list(my_dictionary.items()):
        pretty.append((val,key))

    pretty.sort(reverse=True)

    print(header)
    print(header_sep)
    for key, val in pretty:
        print('{0:^15}{1:^8}'.format(val, key))

def main():
    my_dictionary = {}
    try:
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            process_line(line, my_dictionary)
        pretty_print(my_dictionary)
    except:
            print('File cannot be opened')
            exit()


import string
if __name__ == "__main__":
    main()

