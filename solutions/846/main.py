from typing import List 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        visited = [0]*len(hand)
        for i in range(len(hand)-groupSize+1):
            cardIdx = 1
            if visited[i] == 1:
                continue
            cards = []
            cards.append(i)
            j = i + 1
            while j < len(hand) and cardIdx != groupSize:
                if visited[j] == 0 and hand[j] == hand[cards[-1]] + 1:
                    cards.append(j)
                    cardIdx += 1
                j += 1
            if cardIdx == groupSize:
                for c in cards:
                    visited[c] = 1
            else:
                return False
        if sum(visited) != len(hand):
            return False
        return True

if __name__ == "__main__": 
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    s = Solution()
    assert s.isNStraightHand(hand, groupSize) 
