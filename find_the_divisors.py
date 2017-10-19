# Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's
# divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' 
# (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

def divisors(integer):
  div_list = []
  for i in range(2, (integer - 1)):
    if integer % i == 0:
      div_list.append(i)
    else:
      div_list = div_list
  if len(div_list) == 0:
    return str(integer) + ' is prime'
  else:
    return div_list