def sum_of_squares(num):
      _sum = 0
      n = 1
      while n < num:
           _sum += n**2
           n += 1
      return _sum 
def square_of_sum(num):
       _sum = 0
       n = 1
       while n < num:
           _sum += n
           n += 1 
       return _sum**2 
def square_difference(num):
       return (square_of_sum(num) - sum_of_squares(num))
print(square_difference(100))
