def is_prime(num):
     '''this function checs if num is prime or not.'''
     if num == 1:
         return False
     for i in range(2, num // 2):
          if num % i == 0:
             return False
     return True
def n_th_prime_number(n):
       i = 2
       res = []
       while len(res) < n:
            if is_prime(i):
                 res.append(i)
            i += 1 
       return res[-1]
n = 10001
print(f"{n}-th prime number is: {n_th_prime_number(n)}")
