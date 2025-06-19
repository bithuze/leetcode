from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = [pair[0] for pair in matches]
        loser = [pair[1] for pair in matches]
        not_l=set(winner)-set(loser)
        ans1=sorted(list(not_l))

        counts=Counter(loser)
        ans2=sorted([num for num, count in counts.items() if count == 1])

        return [ans1,ans2]
