class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}

        for i, num in enumerate(nums):
            if target - num in p:
                return [i, p[target - num]]
            p[num] = i
        
