def set_null(*num2):
      '''this function sets null all arguments of function.'''
      for num in num2:
           num = 0
def lst_append(lst, *num):
       '''this function appends *num to the list.'''
       for n in num:
          lst.append(n)
def array_partition(nums):
      '''given an integer array nums of 2n integers, group these integers
      into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of 
      min(ai, bi) for all i is maxsimizedd. this function returns the maximized sum.'''
      n = len(nums) // 2
      _max = []
      _sum = 0
      _sum1 = 0
      _sum2 = 0 
      _sum3 = 0
      _sum4 = 0
      _sum5 = 0
      _sum6 = 0
      _sum7 = 0
      rev_nums = nums[::-1]
      half_nums0 = nums[::2]
      half_nums1 = nums[1::2]
      re_half0 = half_nums0[::-1]
      re_half1 = half_nums1[::-1]
      fr_half = nums[:n]
      se_half = nums[n:]
      rev_fr_half = fr_half[::-1]
      rev_se_half = se_half[::-1]
      for i in range(n):
         _sum += min(half_nums0[i], half_nums1[i])
         _sum1 += min(half_nums0[i], re_half1[i])
         _sum2 += min(re_half0[i], half_nums1[i])
         _sum3 += min(re_half0[i], re_half1[i])
         _sum4 += min(fr_half[i], se_half[i])
         _sum5 += min(fr_half[i], rev_se_half[i])
         _sum6 += min(rev_fr_half[i], se_half[i])
         _sum7 += min(rev_fr_half[i], rev_se_half[i])
      lst_append(_max, _sum, _sum1, _sum2, _sum3, _sum4, _sum5, _sum6, _sum7)
      set_null(_sum, _sum1, _sum2, _sum3, _sum4, _sum5, _sum6, _sum7)
      for j in range(len(fr_half[::2])):
          _sum += min(fr_half[j], se_half[::2][j])
          _sum1 += min(fr_half[::2][j], se_half[j])
          _sum2 += min(rev_fr_half[j], se_half[::2][j])
          _sum3 += min(rev_fr_half[::2][j], se_half[j])
          _sum4 += min(fr_half[j], rev_se_half[::2][j])
          _sum5 +=  min(fr_half[::2][j], rev_se_half[j])
          _sum6 += min(rev_fr_half[j], rev_se_half[::2][j])
          _sum7 += min(rev_fr_half[::2][j], rev_se_half[j])
      m = len(fr_half[1::2])
      M = _max[0]
      for num in _max:
           if num > M:
              M = num 
      return M
print(f"the maxiized sum is: {array_partition([6, 2, 6, 5, 1, 2])}")
