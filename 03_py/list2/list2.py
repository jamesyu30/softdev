#List2 count_evens

def count_evens(nums):
  c = 0 #counter for number of even numbers
  i = 0 #increment for for loop
  for x in nums:
    if nums[i]%2 == 0:
      c += 1
    i += 1
  return c

#returns number of times an even number appears in the nums array
print(count_evens([2,1,2,3,4]))
print(count_evens([2,2,0]))
print(count_evens([1,3,5]))

#List2 big_diff

def big_diff(nums):
  small = nums[0] #initialization for smallest value
  big = nums[0] #initialization for largest value
  for x in nums:
    small = min(small,x)
    big = max(big, x)
  return big-small

#return difference between greatest and least values in nums array
print(big_diff([10,3,5,6]))
print(big_diff([2]))
print(big_diff([7,7,6,8,5,5,6]))

#List2 centered_average

def centered_average(nums):
  small = nums[0] #initialization for smallest value
  big = nums[0] #initialization for largest value
  for x in nums:
    small = min(small,x)
    big = max(big, x)
  total = 0
  for x in nums:
    total += x
  total = total - small -big #removal of smallest and largest values in calculation of average
  return total/(len(nums)-2)

#return average of values in array excluding largest and smallest values
print(centered_average([1,2,3,4,100]))
print(centered_average([-10,-4,-2,-4,-2,0]))
print(centered_average([4,0,100]))

#List2 sum13

def sum13(nums):
  i = 0
  sum = 0
  while(i<len(nums)):
    if(nums[i]!=13):
      sum = sum+nums[i]
      i = i+1
    else:
      i = i+2
  return sum

#return sum of numbers in array excluding 13 and any number immediately after it
print(sum13([1,2,2,1]))
print(sum13([1,1]))
print(sum13([]))

#List2 sum67

def sum67(nums):
  search = 0  #determines if the current numbers are being ignored
  total = 0
  for x in nums:
    if search == 0 and x == 6:
      search = 1
    elif search == 0:
      total += x
    elif search == 1 and x == 7:
      search = 0
  return total

#returns sum of all characters in nums except for those between a 6 and 7 (inclusive)
print(sum67([1,2,2]))
print(sum67([1,2,2,6,99,99,7]))
print(sum67([1,1,6,7,2]))

#List2 has22

def has22(nums):
  i = 0
  while i < len(nums)-1:
    if nums[i] == 2 and nums[i] == nums[i+1]:
      return True
    i += 1
  return False

#returns true if there are two 2's next to each other in nums
print(has22([1,2,2]))
print(has22([1,2,1,2]))
print(has22([1,3,2,2]))
