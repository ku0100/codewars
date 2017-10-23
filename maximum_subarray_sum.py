# The maximum sum subarray problem consists in
# finding the maximum sum of a contiguous subsequence
# in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6

# Easy case is when the list is made up of only positive numbers
# and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.

def maxSequence(arr):
  max_value = 0
  for x in range(0, len(arr)):
    for y in range(1, (len(arr) + 1)):
      value = 0
      for number in arr[x:y]:
        value += number
        if value > max_value:
          max_value = value

  print(max_value)

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])