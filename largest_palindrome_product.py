def is_palindrome(number):
      '''this function return true if number is palindrom and false 
      otherwise. Number is palindrome if it is read same both at the firs and at the and. '''
      num = 0
      cpy_number = number # we copy the number to save original number
      while number != 0:  # creating new number (reversed number of original number)
            num *= 10 
            num += number % 10
            number = number // 10
      return num == cpy_number # checking if original number is equal to reversed number
for num1 in range(999, 100, -1):
      for num2 in range(999, 100, -1):
              num = num1 * num2
              if is_palindrome(num):
                    break
print(f"the largest palindrome prodactconsists of  two three- digits numbers' multipy is: {num}")
