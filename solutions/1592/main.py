class Solution:
    def reorderSpaces(self, text: str) -> str:
        n_space = text.count(' ')
        words = text.split()
        if len(words) > 1: 
            insert_num = n_space // (len(words)-1)
            insert_str = [" "] * insert_num
            append_str = [" "] * (n_space % (len(words)-1))
        else: 
            insert_str = []
            append_str = [" "] * n_space
        insert_str = "".join(insert_str)
        append_str = "".join(append_str)
        res = ""
        for i, w in enumerate(words): 
            res += w 
            if i != len(words)-1:
                res += insert_str
            else: 
                res += append_str
        return res 

if __name__ == "__main__": 
    s = Solution()

    # text = "  this   is  a sentence "
    # assert s.reorderSpaces(text) == "this   is   a   sentence"

    text = "a"
    assert s.reorderSpaces(text) == "a"