class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        ca = 0
        
        for num in nums:
            if c == 0:
                ca = num
            
            if num == ca:
                c += 1
            else:
                c -= 1
        
        return ca
