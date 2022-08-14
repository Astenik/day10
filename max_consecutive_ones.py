def max_consecutive_ones(binary_nums:list):
        '''given a binary array nums as an argument, this function
         returns the maximum number of consecutive 1's in the array.'''
        count = 0
        _max = count
        for num  in binary_nums:
             if num == 1:
                 count += 1 
             else:
                 count = 0
             if count > _max:
                       _max = count
        return _max 
binary_nums = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
print(f"max consecutive ones is equal to: {max_consecutive_ones(binary_nums)}")
