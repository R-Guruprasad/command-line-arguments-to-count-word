'''
Python program for getting the word count from the contents of a file using command line arguments.
Developed by: R.Guruprasad
Ref no:22006697
'''
import sys
count = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        for word in line.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
print(count)
f.close()
