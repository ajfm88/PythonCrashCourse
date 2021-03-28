#You can use the replace() method to replace any word in a
#string with a different word. Here’s a quick example showing how to replace
#'dog' with 'cat' in a sentence:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
#'I really like cats.'
#Read in each line from the file you just created, learning_python.txt, and
#replace the word Python with the name of another language, such as C. Print
#each modified line to the screen.

filename = 'Ch10/learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))