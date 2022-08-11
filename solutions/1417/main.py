class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else: 
                letters.append(ch)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) < len(digits):
            letters, digits = digits, letters
        res = ""
        for i, l in enumerate(letters):
            res += letters[i]
            if len(letters) != len(digits) and i == len(letters)-1:
                continue 
            res += digits[i]
        return res 
