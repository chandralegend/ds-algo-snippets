# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            max_dis = 0
            for i in range(l, r + 1):
                max_dis = max(max_dis, i + nums[i])
            l = r + 1
            r = max_dis
            res += 1
        return res


print(Solution().jump([2, 3, 1, 1, 4]))
