# Given an array of integers, 1 =< a[i] <= n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.

def main():
  arr = [4,3,2,7,8,2,3,1]
  print(removeDuplicates(arr))

def removeDuplicates(nums):
  arr = []
  
  for num in nums:
    if nums.count(num) > 1 and not num in arr:
        arr.append(num)

  return arr


if __name__ == '__main__':
  main()