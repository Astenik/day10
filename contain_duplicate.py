def contain_dulicate(nums:list):
       '''this function return True if any value appears at least
       twice in the array, and return false if every element is distinct.
       Example 1:
          Input: nums = [1, 2, 3, 1]
          Output: True
       Example 2:
          Inpute: nums = [1, 2, 3, 4]
          Output: false.'''
       for ind in range(len(nums)):  # iterates over the list.
            for ind1 in range(ind + 1, len(nums)):  # iterates over the list starts with ind + 1.
                  if nums[ind] == nums[ind1]:  # checs if nums[ind] element has duplicate or not.
                        return True
       return False 
nums = [1, 3, 5, 3, 6, 7]
print(f"Does your list countain duplicates? {contain_dulicate(nums)}")
