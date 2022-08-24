def missing_number(nums:list):
        '''given an array nums (as parametre) containing n distinct numbers
        in the range [0, n], this function returns the only number in the 
        range that is missing from the array.'''
        for i in range(len(nums)):
          if nums[i] != i:
              return i 
nums = [1, 0, 3, 2, 8, 6, 7, 4, 9]
print(f"the missing number is: {missing_number(nums)}")
