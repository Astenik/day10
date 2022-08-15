def array_partition(nums):
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
      _max.append(_sum)
      _max.append(_sum1)
      _max.append(_sum2)
      _max.append(_sum3)
      _max.append(_sum4)
      _max.append(_sum5)
      _max.append(_sum6)
      _max.append(_sum7)
      M = _max[0]
      for num in _max:
           if num > M:
              M = num 
      return M
print(array_partition([6, 2, 6, 5, 1, 2]))
