class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            l=False
            for start ,end in ranges:
                if start <= i <= end:
                    l=True
            if not l:
                return False
        return True
            
            
