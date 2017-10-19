# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
  longest = ''.join(strarr[0:k])
  x = 0
  n = len(strarr)
  print(k<=0)
  if n == 0:
    return ""
  elif n < k:
    return ""
  elif k <= 0:
    return ""
  else:
    while x < (n):
      if len(''.join(strarr[x:(x+k)])) > len(longest):
        longest = ''.join(strarr[x:(x+k)])
        x += 1
      else:
        x += 1
 return longest


longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)