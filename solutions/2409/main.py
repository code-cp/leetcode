from typing import * 

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arr_a = arriveAlice.split("-")
        arr_a = [int(x) for x in arr_a]
        arr_b = arriveBob.split("-")
        arr_b = [int(x) for x in arr_b]
        lea_a = leaveAlice.split("-")
        lea_a = [int(x) for x in lea_a]
        lea_b = leaveBob.split("-")
        lea_b = [int(x) for x in lea_b]

        arr_a_day = 0
        for i in range(arr_a[0]-1):
            arr_a_day += days[i]
        arr_a_day += arr_a[1]

        arr_b_day = 0
        for i in range(arr_b[0]-1):
            arr_b_day += days[i]
        arr_b_day += arr_b[1]
        
        lea_a_day = 0
        for i in range(lea_a[0]-1):
            lea_a_day += days[i]
        lea_a_day += lea_a[1]

        lea_b_day = 0
        for i in range(lea_b[0]-1):
            lea_b_day += days[i]
        lea_b_day += lea_b[1]
        
        if lea_a_day < arr_b_day:
            return 0 
        if lea_b_day < arr_a_day: 
            return 0 
        
        max_arr = max(arr_a_day, arr_b_day)
        min_lea = min(lea_a_day, lea_b_day)
        
        if max_arr <= min_lea: 
            return min_lea - max_arr + 1 
        else: 
            return 0                     

if __name__ == "__main__": 
    s = Solution() 

    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-16"
    assert s.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == 1

    # arriveAlice = "10-01"
    # leaveAlice = "10-31"
    # arriveBob = "11-01"
    # leaveBob = "12-31"
    # assert s.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == 0
    
    # arriveAlice = "08-15"
    # leaveAlice = "08-18"
    # arriveBob = "08-16"
    # leaveBob = "08-19"
    # assert s.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob) == 3 