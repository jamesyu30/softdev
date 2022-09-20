#Warm up 1 sleep in

def sleep_in(weekday, vacation):
  if(weekday==False or vacation==True):
    return True
  else:
      return False

#Warm up 1 monkey trouble

def monkey_trouble(a_smile, b_smile):
  if((a_smile and b_smile) or (a_smile == False and b_smile == False)):
    return True
  else:
    return False

#Warm up 1 sum_double

def sum_double(a, b):
  if a==b:
    return a*4
  else:
    return a+b

#Warm up 1 diff21

def diff21(n):
  if n>21:
    return 2*abs(n-21)
  else:
    return abs(n-21)

 #Warm up 1 parrot trouble

 def parrot_trouble(talking, hour):
  if(hour<7 or hour>20):
    if(talking):
      return True
    else:
      return False
  else:
    return False

 #Warm up 1 makes 10

 def makes10(a, b):
  if(a+b == 10):
    return True
  if(a ==  10 or b == 10):
    return True
  else:
    return False

 #Warm up 1 near hundred

 def near_hundred(n):
  if(abs(100 - n) <=10 or abs(200 - n) <=10):
    return True
  else:
    return False

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

#Warm up 1 not string

def not_string(str):
  if(str[0:3] == 'not'):
    return str
  else:
    return 'not ' + str

#warm up 1 missing char

def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

#Warm up 1 front_back

def front_back(str):
  if(len(str)==1):
    return str
  else:
    return str[len(str)-1:]  + str[1:len(str)-1] + str[:1]

#Warm up 1 front3

def front3(str):
  if(len(str)<3):
    return str*3
  else:
    return str[:3]*3
