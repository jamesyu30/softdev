#Warm up 1 sleep in

def sleep_in(weekday, vacation):
  if(weekday==False or vacation==True):
    return True
  else:
      return False

#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
print(sleep_in(False,False))
print(sleep_in(True,False))
print(sleep_in(False,True))

#Warm up 1 monkey trouble

def monkey_trouble(a_smile, b_smile):
  if((a_smile and b_smile) or (a_smile == False and b_smile == False)):
    return True
  else:
    return False

#We are in trouble if they are both smiling or if neither of them is smiling.
#Return True if we are in trouble.
print(monkey_trouble(True, True))
print(monkey_trouble(False, True))
print(monkey_trouble(False, False))

#Warm up 1 sum_double

def sum_double(a, b):
  if a==b:
    return a*4
  else:
    return a+b

#Given two int values, return their sum.
#Unless the two values are the same, then return double their sum.
print(sum_double(1,2))
print(sum_double(2,2))
print(sum_double(3,4))

#Warm up 1 diff21

def diff21(n):
  if n>21:
    return 2*abs(n-21)
  else:
    return abs(n-21)

#return the absolute difference between n and 21,
#except return double the absolute difference if n is over 21.
print(diff21(17))
print(diff21(21))
print(diff21(23))

#Warm up 1 parrot trouble

def parrot_trouble(talking, hour):
  if(hour<7 or hour>20):
    if(talking):
      return True
    else:
      return False
  else:
    return False

#return true if talking is true and hour is before 7 or after 20
print(parrot_trouble(True,6))
print(parrot_trouble(True,8))
print(parrot_trouble(False,6))

#Warm up 1 makes 10

def makes10(a, b):
  if(a+b == 10):
    return True
  if(a ==  10 or b == 10):
    return True
  else:
    return False

#return if one of them is 10 or they add up to 10
print(makes10(10,7))
print(makes10(3,7))
print(makes10(1,2))

 #Warm up 1 near hundred

def near_hundred(n):
  if(abs(100 - n) <=10 or abs(200 - n) <=10):
    return True
  else:
    return False

#returns if a number is within 10 of 100 or 200
print(near_hundred(199))
print(near_hundred(101))
print(near_hundred(399))
#Warm up 1 pos_neg

def pos_neg(a, b, negative):
  if negative:
    if(a<0 and b<0):
      return True
    else:
      return False
  elif(a<0 and b>0) or (a>0 and b<0):
    return True
  else:
    return False

#true if one is + and the other is - unless if negative is negative
#then only return true if both are -
print(pos_neg(1,-1,False))
print(pos_neg(-1,-1,False))
print(pos_neg(-1,-1,True))

#Warm up 1 not string

def not_string(str):
  if(str[0:3] == 'not'):
    return str
  else:
    return 'not ' + str

#adds not to front of the string
print(not_string("apple"))
print(not_string("not apple"))

#warm up 1 missing char

def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

#remove a char at index n
print(missing_char("missing",3))
print(missing_char("hi",0))
print(missing_char("cate",3))

#Warm up 1 front_back

def front_back(str):
  if(len(str)==1):
    return str
  else:
    return str[len(str)-1:]  + str[1:len(str)-1] + str[:1]

#swaps first and last characters
print(front_back("ih"))
print(front_back("pear"))
print(front_back("eppla"))

#Warm up 1 front3

def front3(str):
  if(len(str)<3):
    return str*3
  else:
    return str[:3]*3

#returns a string with three copies of the first three characters
print(front3("happy"))
print(front3("hi"))
print(front3("z"))
