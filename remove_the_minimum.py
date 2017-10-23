# Task

# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with a lower index.
# If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

def remove_smallest(numbers):
  final_array = numbers
  if len(final_array) == 0:
    return []
  else:  
    min_value = min(final_array)

  if final_array.count(min_value) > 1:
    final_array.remove(final_array[final_array.index(min_value)])
  else:
    final_array.remove(min_value)

  return final_array

remove_smallest([1,2,3,4,5,1,1])