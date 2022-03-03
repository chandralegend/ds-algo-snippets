from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False

        sum_arr = sum_arr // 3
        left_sum = 0
        for i in range(len(arr)):
            left_sum += arr[i]
            if left_sum == sum_arr:
                left_sum = 0
                continue
            if left_sum > sum_arr:
                return False
        return True


arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
print("Solution:", Solution().canThreePartsEqualSum(arr))
