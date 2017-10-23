# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# The returned format must be correct in order to complete this challenge. 
# Don't forget the space after the closing parenthesis!

def create_phone_number(n):
  x = 0
  phone_number = "("
  while x < 3:
    phone_number = phone_number + str(n[x])
    x += 1
  phone_number = phone_number + ") "
  while x < 6:
    phone_number = phone_number + str(n[x])
    x += 1
  phone_number = phone_number + "-"
  while x < 10:
    phone_number = phone_number + str(n[x])
    x += 1

  print(phone_number)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])