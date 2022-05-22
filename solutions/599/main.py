from typing import * 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rest1 = DefaultDict(int)
        ans = []
        min_sum = float("inf")
        for i, r in enumerate(list1): 
            rest1[r] = i 
        for i, r in enumerate(list2): 
            # O(1) time to search in hashmap 
            if r in rest1: 
                v = rest1[r]
                if min_sum > i + v:
                    min_sum = i + v 
                    ans = []
                    ans.append(r)
                elif min_sum == i + v: 
                    ans.append(r)
        return ans 

if __name__ == "__main__": 
    s = Solution()

    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    result = s.findRestaurant(list1, list2)
    assert result == ["Shogun"]

    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    result = s.findRestaurant(list1, list2)
    assert result == ["Shogun"]