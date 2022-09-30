import random
'''
Coding Cobras - James Yu, Thomas Zhang
Softdev
2022-09-30
Time Spent: 1.6 hours

DISCO: readline() reads one character at a time and readlines() splits a file into lines
       rsplit splits from the right
       Split has a second parameter which determines how many times you split
       when inputting a file as a parameter you need quotes
       python has floats and ints like java
QCC:
HOW THIS SCRIPT WORKS: It takes the file and puts each line into a list.
Then, slices the first and last elements of the list(to get rid of the extra parts).
Next, we split the last comma so the list looks like this: [job,percent].
Finally, We add the first index of the list as the key and the second as the value, using strip to remove the new line.

weighted choice gets a list of all of the percentages from a dictionary.
It gets fed into the random.choices function that takes a list of choice and the weights(list of percentages mentioned earlier) and returns a job 
'''

def to_dict(file):
    csv = open(file,"r")
    split = csv.readlines()#reads each individual line
    split = split[1:len(split)-1]#gets rid of first and last lines
    #print(split)
    csv.close()
    jobs = {}
    for line in split:
        data = line.rsplit(",",1)#split the last comma and split only once
        #print(data)
        jobs[data[0]] = float(data[1].strip())#strip gets rid of new line, float converts the string into a number
    return jobs # returns a dict with job:percent

def weighted_choice(d):
    weight = list(d.values())#list of all of the percentages
    return random.choices(list(d.keys()),weights=weight)[0]#random.choices has two parameters: the choices, and the weights. The weights are respective to the choices.
    #[0] makes it return a string not a list (Sales instead of ['Sales'])

print(weighted_choice(to_dict("occupations.csv")))

def prob_tester(tries):#tests if choices are weighted accurately
    i = 0
    index = 0
    prob = {}
    while i<tries:
        job = weighted_choice(to_dict("occupations.csv"))#choosing a random job
        if job in prob.keys():#checks in job is already a key in the dictionary
            prob[job] = float(prob.get(job)+(1/tries*100))#if it is add 1/tries (*100 is for percentage 1/10000 (1/100 is the percentage)). get(key) returns the value of the key
        else:
            prob[job] = float(1/tries*100)#if not create it and make the value 1
        i = i+1
    return prob

print(prob_tester(100000))
        
