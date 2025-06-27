class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t=set(nums)
        if len(nums)== len(t):
            return False 
        else:
            return True 
