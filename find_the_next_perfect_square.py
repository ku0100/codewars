# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

def find_next_square(sq):
  # Return the next square if sq is a square, -1 otherwise
  i = sq**(0.5)
  if i % 1 == 0:
    i += 1
    return i * i
  else:
    return -1