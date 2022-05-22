from typing import List 

class Solution:
    def __init__(self):
        self.max_total = 0

    def backtracking(self, statements, player, good, bad):
        # base case
        if player == len(statements):
            self.max_total = max(len(good), self.max_total)
            return

        # backtracking
        for i in range(player, len(statements)):
            # prune
            if i in bad:
                continue

            new_good = [j for j in range(len(statements[i])) if statements[i][j] == 1]
            new_good.append(i)
            new_bad = [j for j in range(len(statements[i])) if statements[i][j] == 0]

            new_good = [x for x in new_good if x not in good]
            new_bad = [x for x in new_bad if x not in bad]

            if len(set(good+new_good).intersection(set(bad+new_bad))) > 0:
                pass
            else:
                self.backtracking(statements, player+1, good+new_good, bad+new_bad)
            if i not in bad:
                bad.append(i)

        if len(set(good).intersection(set(bad))) > 0:
            pass
        else:
            self.max_total = max(len(good), self.max_total)

        return

    def maximumGood(self, statements: List[List[int]]) -> int:
        self.backtracking(statements, 0, [], [])
        return self.max_total

if __name__ == "__main__":
    statements = [[2,1,2],[1,2,2],[2,0,2]]
    s = Solution()
    assert s.maximumGood(statements) == 2
