'''
Coding Cobras - James Yu, Thomas Zhang 
DISCO: readline() reads one character at a time and readlines() splits a file into lines
split parameter
QCC:
HOW THIS SCRIPT WORKS:
'''

def to_dict():
    csv = open("occupations.csv","r")
    split = csv.readlines()
    for line in split:
        data = line.rsplit(",",1)
        print(data[1])
        #print(split)
    
to_dict()
