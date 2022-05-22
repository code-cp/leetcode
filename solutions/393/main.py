from typing import * 

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_data = 0 
        mask1 = 1 << 7
        mask2 = 1 << 6
        while n_data < len(data):  
            mask = 1 << 7 
            num = data[n_data]
            if mask & num == 0: 
                # format is 0xxxx
                n_data += 1
            else: 
                # format is 1xxx10xxx0
                n_bytes = 0
                while mask & num: 
                    n_bytes += 1 
                    mask = mask >> 1; 
                if n_bytes < 2 or n_bytes > 4: 
                    return False 
                n_data += 1 
                for j in range(n_bytes-1):
                    if n_data + j > len(data) - 1:  
                        return False 
                    num = data[n_data + j] 
                    # first two are 10 
                    if num & mask1 and not (num & mask2): 
                        continue  
                    else: 
                        return False 
                n_data += n_bytes - 1
        return True 

if __name__ == "__main__": 
    s = Solution()

    data = [197,130,1]
    assert s.validUtf8(data)

    data = [255]
    assert not s.validUtf8(data)

    data = [145]
    assert not s.validUtf8(data)

    data = [250,145,145,145,145]
    assert not s.validUtf8(data)