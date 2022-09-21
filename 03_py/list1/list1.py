#first last 6

def first_last6(nums):
  return (nums[0] == 6 or nums[len(nums)-1]==6)

#returns if the first or last element in the list is 6
print(first_last6([1,2,3]))
print(first_last6([6,2,3]))
print(first_last6([6,2,6]))

#same first last

def same_first_last(nums):
  return (len(nums)>= 1 and nums[0] == nums[len(nums)-1])

#checks if the array has a length greater than or equal to 1
#and if the first and last elements are equal
print(same_first_last([1,2,3]))
print(same_first_last([]))
print(same_first_last([3,2,3]))

#make pi

def make_pi():
  return [3,1,4]

#returning a pi array
print(make_pi())

#common end

def common_end(a, b):
  return (a[0] == b[0] or a[len(a)-1] == b[len(b)-1])

#checks if the first or last elements of the two arrays are the same
print(common_end([1,2,3],[1,4]))
print(common_end([1,2,3],[5,4]))
print(common_end([1,2,3],[1,3]))

#sum3

def sum3(nums):
  s = 0
  for x in nums:
    s = s+x
  return s

#adds up the elements in the list
print(sum3([1,2,3]))
print(sum3([10,15,20]))
print(sum3([3,3,3]))

#rotateleft3

def rotate_left3(nums):
  return nums[1:] + nums[:1]

#moves the first element to the back

#can't do nums[0] because it returns an int
#but you can do nums[:1] because it returns a list - can only cat strings and lists

print(rotate_left3([1,2,3]))
print(rotate_left3([2,3,1]))
print(rotate_left3([10,8,9]))

#reverse3

def reverse3(nums):
  return nums[::-1]

#reverses list
print(reverse3([3,2,1]))
print(reverse3([1,2,3]))
print(reverse3([7,3,5,6,1]))

#max end3
def max_end3(nums):
  if (nums[0]>nums[-1]):
    return [nums[0],nums[0],nums[0]]
  else:
    return [nums[-1],nums[-1],nums[-1]]
#nums[-1] accesses the last element
#returns a list with a length of 3 of the biggest between the first and last element
print(max_end3([1,3,7]))
print(max_end3([1,2,3]))
print(max_end3([9,3,7]))

#sum2

def sum2(nums):
  if(len(nums)==0):
    return 0
  if(len(nums) < 2):
    return nums[0]
  return nums[0]+nums[1]

#adds the first two elements of a list
print(sum2([]))
print(sum2([12]))
print(sum2([5,10,20]))

#middle way

def middle_way(a, b):
  return a[1:2]+b[1:2]

#returns a list with the middle element of both lists
print(middle_way([1,1,1],[3,2,3]))
print(middle_way([4,5,6],[2,2,2]))
print(middle_way([1,2,3],[8,9,10]))

#make ends

def make_ends(nums):
  return nums[:1]+nums[len(nums)-1:]

#returns a list with the first and last elements
print(make_ends([1,2,3]))
print(make_ends([9,2,9]))
print(make_ends([6,2,4]))

#has 23

def has23(nums):
  return (nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3)

#returns if the array contains 2 or 3
print(has23([1,4]))
print(has23([2,3]))
print(has23([1,2]))

