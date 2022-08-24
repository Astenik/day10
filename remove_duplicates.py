'''this project removes duplicate numbers from non- decreacing list.'''
def douplicate_indexes(nums):
     '''this function returns duplicates numbers' indexes'''
     for i in range(len(nums)):
          for ii in range(len(nums) - 1):
              if nums[ii] == nums[ii + 1]:
                   for j in range(ii, len(nums) - 1):
                       nums[j] = nums[j + 1]
                   nums[-1] = '_'
      return nums 
print(remove_duplicate([1, 1, 2, 3, 4, 4, 4, 5]))
