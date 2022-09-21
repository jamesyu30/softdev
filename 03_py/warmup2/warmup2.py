#Warm up 2 string_times

def string_times(str, n):
  return str*n

#Warm up 2 front times

def front_times(str, n):
  if (len(str)<3):
    return str*n
  else:
    return str[:3]*n

#warm up 2 string bits

def string_bits(str):
  index  = 0
  s = ""
  while(index<len(str)):
      s = s+str[index]
      index = index + 2
  return s

print(string_bits("abcdef"))
print(string_bits("hello"))
print(string_bits("123456"))

#warm up 2 string_splosion

def string_splosion(str):
  i = 0
  s = ""
  for x in str:
    s = s+str[:i+1]
    i = i+1
  return s

print(string_splosion("python"))
print(string_splosion("java"))
print(string_splosion("Soft"))

#warm up 2 last2

def last2(str):
  s = str[len(str)-2:]
  i = 0
  c = 0
  while (i<len(str)-2):
    if (s == str[i:i+2]):
      c = c+1
    i = i + 1
  return c

print(last2("hixxhi"))
print(last2("xxxx"))
print(last2("11212"))

#array count9

def array_count9(nums):
  c = 0
  for x in nums:
    if x==9:
      c = c+1
  return c

print(array_count9([1,2,9]))
print(array_count9([1,9,9]))
print(array_count9([9,9,9]))

#array front9

def array_front9(nums):
  i = 0
  while (i<4 and i<len(nums)):
    if nums[i] == 9:
      return True
    i = i+1
  return False

print(array_front9([1,1,1,1,1]))
print(array_front9([1,1,1,1,9]))
print(array_front9([1,1,9]))

#warmup 2 array123

def array123(nums):
  i = 0
  for x in nums:
    if (nums[i:i+3] == [1,2,3]):
      return True
    i = i+1
  return False

print(array123([1,1,2,3,1]))
print(array123([1,1,2,4,1]))
print(array123([1,1,2,3,1,2,3]))

#warmup 2 string match

def string_match(a, b):
  i = 0
  c = 0
  while(i<len(a)-1):
    if (a[i:i+2] == b[i:i+2]):
      c = c+1
    i = i+1
  return c

print(string_match("abc","abc"))
print(string_match("h","hello"))
print(string_match("","hello"))
