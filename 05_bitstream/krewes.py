"""
James Yu
SoftDev
k05--convert txt file into a dictionary
2022-9-29
Time Spent: 1.1 hours

DISCO: int() typecasts a string to int
       when spliting you need to set the result to a new variable
       dict[key].append() adds a value to a key
QCC:
OPS SUMMARY: First, open the file using open(). f.read() imports the content of the text file.
I split the text into each devo's info. Then, loop through the entire list of each person's
info and split it into another list. The new list has the period, devo, ducky separated. Lastly,
add a list containing name and ducky to the key(period).

To pick randomly, we chose a random list in a key and print the key and the elements of the selected list
"""
import random
def to_dict():
    f = open("krewes.txt","r")
    t = f.read().split("@@@") #reads and splits the text into each devo (['2$$$devo$$$ducky', '7$$$devo2$$$ducky2', '8$$$devo3$$$ducky3', '\n'])
    i = 0
    krewes = {2:[],7:[],8:[]}
    #print(t)
    while i<len(t)-1:
        t2 = t[i].split("$$$") #separates into [pd,devo,ducky]
        #print(t2)
        krewes[int(t2[0])].append([t2[1],t2[2]]) #int(t2[0]) gives the period, t2[1] and t2[2] is name and ducky, makes a 2d array within each key
        #print(krewes)
        i = i+1
    return krewes

def random_devo (d): #d is the dictionary (in this case krewes)
    randKey = random.choice(list(d.keys()))
    l = len(d[randKey])
    info = d[randKey][random.randrange(0,l,1)]#a list with a random name and dname
    return "Period: "+ str(randKey) + " Name: " + info[0] + " DName: "+info[1]

print(random_devo(to_dict()))
        
    



