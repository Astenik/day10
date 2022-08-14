def is_divided(num):
     if (num % 5 == 0) and (num % 7 == 0) and (num % 9 == 0) and (num % 19 == 0):
          if (num % 11 == 0) and (num % 13 == 0) and (num % 16 == 0) and (num % 17 == 0):
               return True
     return False 
def smallest_multiple():
      '''2520 is the smallest number that can be divided by each
        of the numbers from 1 to 10 without any remainder. This function returns the
        smallest positive number that is evenly divisible by all of the numbers
         from 1 to 20.'''
      num = 2000
      while not is_divided(num):
             num += 1 
      return num 
print(f"the smallest multiple is: {smallest_multiple()}")
