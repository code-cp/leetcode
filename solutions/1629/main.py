from typing import List 

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = ""
        maxTime = 0
        for i in range(len(releaseTimes)):
            if i == 0:
                time = releaseTimes[i]
            else:
                time = releaseTimes[i] - releaseTimes[i-1]
            if time > maxTime:
                maxTime = time
                result = keysPressed[i]
            elif time == maxTime:
                if ord(keysPressed[i]) > ord(result):
                    result = keysPressed[i]
        return result

if __name__ == "__main__": 
    releaseTimes = [9,29,49,50]
    keysPressed = "cbcd"
    s = Solution()
    assert s.slowestKey(releaseTimes, keysPressed) == "c"
