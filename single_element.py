def single_element(nums):
     '''this function findes the element that is contained in array nums only one time: others is contained two times.'''
     for ind1 in range(len(nums)):
          for ind2 in range(ind1 + 1, len(nums)):
              if nums[ind1] == nums[ind2]: # checs if nums[ind1] element repeted in list
                   break
          else:
              return nums[ind1] # if nums[ind1] has no duplicate in list return nums[ind1]
nums =[1, 3, 4, 2, 4, 2, 1]
print(f"single element of your list is: {single_element(nums)}")
