from typing import * 
   
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        
        prefix_alpha = [0]*(n+1)
        prefix_digit = [0]*(n+1)
        diff = [0]*(n+1)
        map_diff = {0: 0}
        for i in range(n): 
            if array[i].isalpha():
                prefix_alpha[i+1] = prefix_alpha[i] + 1 
                prefix_digit[i+1] = prefix_digit[i]
            else: 
                prefix_alpha[i+1] = prefix_alpha[i]
                prefix_digit[i+1] = prefix_digit[i] + 1 
            diff = prefix_alpha[i+1] - prefix_digit[i+1]
            # only record left most position of each diff value  
            if map_diff.get(diff, -1) == -1:
                map_diff[diff] = i + 1 

        res = ""    
        for i in range(n):
            cur_diff = prefix_alpha[i+1] - prefix_digit[i+1]
            if map_diff.get(cur_diff, -1) != -1: 
                j = map_diff[cur_diff] 
                if i+1-j > len(res): 
                    res = array[j:i+1]
                    
        return list(res)

if __name__ == "__main__": 
    s = Solution() 

    array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
    assert s.findLongestSubarray(array) == ["52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5"]
    
    # array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    # assert s.findLongestSubarray(array) == ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]