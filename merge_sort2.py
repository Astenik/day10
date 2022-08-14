def merge_sort(nums):
     '''this function sorts the nums list using merge sort algorithm.'''
     if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(right)
        merge_sort(left)
        i = j = k = 0
        while i < len(left) and j < len(right):
              if left[i] < right[j]:
                 nums[k] = left[i] 
                 i += 1
              else:
                  nums[k] = right[j] 
                  j += 1 
              k += 1
        while i < len(left):
              nums[k] = left[i]
              i += 1
              k += 1
        while j < len(right):
               nums[k] = right[j]
               j += 1
               k += 1
     return nums
def merged(nums1, nums2):
    '''this function returns new sorted list consists of two lists: nums1 and nums2.'''
    m = len(nums2) - 1
    n = len(nums1) - m 
    j = 0
    for i in range(n - 1, n + m):
       nums1[i] = nums2[j]
       j += 1
    return merge_sort(nums1)
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(f' your sorted list consists of nums1 and nums2 lists is: {merged(nums1, nums2)}')
