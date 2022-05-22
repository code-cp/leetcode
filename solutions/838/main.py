class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        right_on_left = [N] * N
        right_on_right = [N] * N
        left_on_left = [N] * N
        left_on_right = [N] * N
        pre_l, pre_r = -1, -1
        for i in range(N): 
            if dominoes[i] == "R": 
                pre_r = i 
            elif pre_r != -1: 
                right_on_left[i] = i-pre_r
            if dominoes[i] == "L":
                pre_l = i 
            elif pre_l != -1: 
                left_on_left[i] = i-pre_l
        pre_l, pre_r = -1, -1
        for i in range(N-1, -1, -1): 
            if dominoes[i] == "L": 
                pre_l = i
            elif pre_l != -1: 
                left_on_right[i] = -(i-pre_l)
            if dominoes[i] == "R": 
                pre_r = i
            elif pre_r != -1: 
                right_on_right[i] = -(i-pre_r)
        result = ""
        for i in range(N): 
            if dominoes[i] == "R": 
                result += "R" 
            elif dominoes[i] == "L": 
                result += "L"
            else: 
                left_force, right_force = 0, 0 
                if right_on_left[i] >= left_on_left[i]: 
                    right_force = 0 
                else: 
                    right_force = N-right_on_left[i]
                if left_on_right[i] >= right_on_right[i]:
                    left_force = 0 
                else: 
                    left_force = N-left_on_right[i]
                if left_force == right_force:
                    result += "."
                elif left_force < right_force:
                    result += "R"
                else: 
                    result += "L"
        return result 
                  
if __name__ == "__main__": 
    s = Solution()
    dominoes = ".L.R...LR..L.."
    assert s.pushDominoes(dominoes) == "LL.RR.LLRRLL.."
    dominoes = "L.....RR.RL.....L.R."
    assert s.pushDominoes(dominoes) == "L.....RRRRLLLLLLL.RR"
    dominoes = ".L.R...LR..L.."
    assert s.pushDominoes(dominoes) == "LL.RR.LLRRLL.."