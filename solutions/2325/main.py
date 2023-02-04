class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {}
        count = 0 
        for k in key: 
            if count == 26: 
                break 
            if k == " ":
                continue 
            if decode.get(k, -1) == -1:
                decode[k] = count 
                count += 1 
        res = ""
        for m in message: 
            if m == " ":
                res += " "
                continue 
            res += chr(decode[m]+ord("a"))
        return res 

if __name__ == "__main__": 
    s = Solution() 

    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    assert s.decodeMessage(key, message) == "this is a secret"