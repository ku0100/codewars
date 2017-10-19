# In this kata, you must create a digital root function.

# A digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has two digits,
# continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# Here's how it works (Ruby example given):

def digital_root(n):
  x = str(n)
  sum = 0
  for i in range(0, len(x)):
    sum += int(x[i])
  if len(str(sum)) > 1:
    digital_root(sum)
  else:
    return sum
