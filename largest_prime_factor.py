def is_prime(num):
     '''this function checs if num is prime or not.'''
     if num == 1:
         return False
     for i in range(2, num // 2):
          if num % i == 0:
             return False
     return True
def max_prime_factor(num):
     '''this function findes larges prime factor of number.'''
     max_prime = 2
     for i in range(2, num // 2):
          if num % i == 0 and is_prime(i):
              max_prime = i
     return max_prime
number = 600851475143
print(f'the larges prime factor of {number} is: {max_prime_factor(number)}')
