def array_partition(nums):
      '''Given an integer array nums of 2n integers, group these 
      integers into n pairs (a1, b1), (a2, b2), ... , (an, bn) such that the sum of 
      min(ai, bi) for all i is maximized. These function returns the maximized sum.'''
      n = len(nums) // 2
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                count += 1 
        if count == 0:
            break 
    nums1 = nums[::2]
    nums2 = nums[1::2]
    _sum = 0
    for i in range(n):
        _sum += min(nums1[i], nums2[i])
    return _sum 
nums = [6, 2, 6, 5, 1, 2]
print(f"the maxiized sum is: {array_partition(nums)}")
