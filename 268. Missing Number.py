class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ren=[i for i in range(n+1)]
        set_n=set(nums)
        for i in ren:
            if i not in set_n:
                return i
