def min_(nums):
     m = nums[0]
     for num in nums:
         if num < m:
             m = num
     return m
def array_partition(nums):
      n = len(nums) // 2
      lst = []
      my_dict = {f'{0}': lst}
      for i in range(len(nums) - 1):
          lst = []
          for j in range(i + 1, len(nums)):
               lst.append((nums[i], nums[j]))
          my_dict[f'{i}'] = lst 
      res = []
      for key in my_dict:
           _max = 1
           for num in my_dict[key]:
               if min_(num) > _max:
                    _max = min_(num)
           res.append(_max)
      for ii in range(len(res)):
          for jj in range(len(res) - ii - 1):
               if res[jj] < res[jj + 1]:
                   res[jj], res[jj + 1] = res[jj + 1], res[jj]
      _sum = 0
      for k in range(n):
          _sum += res[k]
      return _sum 
print(array_partition([1, 4, 3, 2]))
