import random
"""
James YU
SoftDev
k<nn>--<Title>
2022 9 22
Time Spent:

DISCO: Don't use existing function names like random
QCC:
OPS SUMMARY:
"""

krewes = {2:["awong30","bchen30","cchen33"],7:["afang30","dchen30","gpark30"],8:["ali34","bwang30","eli30"]}

def randomK ():
    randKey = random.randrange(0,3,1)
    print(randKey)
    return krewes[randKey]

print(randomK())