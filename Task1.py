"""
Problem:
Given an array of integers, nums, and an integer target, please find the two integers in the array, and target, and return their array subscripts.
"""

from typing import List

class Solution1:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
      for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
          return [i, j]
          return []

solution1 = Solution1()
solution1.twoSum([2,7,11,15],18)
time(solution1.twoSum([2,7,11,15],18))

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

solution2 = Solution2()
solution2.twoSum([2,7,11,15],18)
time(solution2.twoSum([2,7,11,15],18))
