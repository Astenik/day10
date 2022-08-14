'''this project removes duplicate numbers from non- decreacing list.'''
def douplicate_indexes(nums):
     '''this function returns duplicates numbers' indexes'''
     res =[]
     for i in range(len(nums)):
         for j in range(i + 1, len(nums)):
              if nums[i] == nums[j]:
                    res.append(j)
                    break
     return res 
numbers = [1, 1, 1, 3, 5, 6, 7, 7] 
indexes = douplicate_indexes(numbers)
print(indexes)
ind = 0
while ind < len(indexes):
    if ind  == 0:
       for i in range(indexes[ind], len(numbers) - 1):
             numbers[i] = numbers[i + 1] # moves every element to left from doplicate index
    else:
         for i in range(indexes[ind] - 1 - ind, len(numbers) - 1):
             numbers[i] = numbers[i + 1] # moves every element to left from doplicate index
    numbers[-1] = '_'
    ind += 1
print(numbers)
