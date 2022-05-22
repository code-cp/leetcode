import heapq 
from collections import defaultdict

# TLE 

class State:
    def __init__(self, nextIdx, strLen, hasLower, hasUpper, hasDigit, secLastCh, lastCh, cost):
        self.nextIdx = nextIdx 
        self.strLen = strLen 
        self.hasLower = hasLower
        self.hasUpper = hasUpper
        self.hasDigit = hasDigit
        self.secLastCh = secLastCh
        self.lastCh = lastCh
        self.cost = cost

checkLen = lambda x: x >= 6 and x <= 20
checkStatus = lambda x, y, z: x and y and z 
checkRepeat = lambda x, y, z: x == y and z == y  

def addChar(minCost, pq, state, ch, allStates, new_cost, nextIdx):
    if checkRepeat(state.secLastCh, state.lastCh, ch): 
        return False 
    hasLower = state.hasLower or ch.islower()
    hasUpper = state.hasUpper or ch.isupper()
    hasDigit = state.hasDigit or ch.isdigit()
    newState = State(nextIdx, state.strLen+1, hasLower, hasUpper, hasDigit, state.lastCh, ch, new_cost)
    if minCost[id(newState)] != None:
        if minCost[id(newState)] <= newState.cost:
            return False 
    heapq.heappush(pq, (newState.cost, id(newState)))
    allStates[id(newState)] = newState 
    minCost[id(newState)] = newState.cost
    return True 

def delChar(minCost, pq, state, allStates):
    newState = State(state.nextIdx+1, state.strLen, state.hasLower, state.hasUpper, state.hasDigit, state.secLastCh, state.lastCh, state.cost+1)
    if minCost[id(newState)] != None:
        if minCost[id(newState)] <= newState.cost:
            return False 
    heapq.heappush(pq, (newState.cost, id(newState)))
    allStates[id(newState)] = newState 
    minCost[id(newState)] = newState.cost
    return True 

def replaceChar(minCost, pq, state, ch, allStates):
    if checkRepeat(state.secLastCh, state.lastCh, ch): 
        return False 
    hasLower = state.hasLower or ch.islower()
    hasUpper = state.hasUpper or ch.isupper()
    hasDigit = state.hasDigit or ch.isdigit()
    newState = State(state.nextIdx+1, state.strLen+1, hasLower, hasUpper, hasDigit, state.lastCh, ch, state.cost+1)
    if minCost[id(newState)] != None:
        if minCost[id(newState)] <= newState.cost:
            return False 
    heapq.heappush(pq, (newState.cost, id(newState)))
    allStates[id(newState)] = newState 
    minCost[id(newState)] = newState.cost
    return True  

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        pq = []
        state = State(0, 0, False, False, False, None, None, 0)
        heapq.heappush(pq, (state.cost, id(state))) 
        allStates = defaultdict(lambda: None) 
        allStates[id(state)] = state 
        minCost = defaultdict(lambda: None) 
        minCost[id(state)] = state.cost 
        while len(pq) > 0: 
            # get min cost state 
            _, stateIdx = heapq.heappop(pq)
            state = allStates[stateIdx] 
            # check if lower cost exists  
            if minCost[id(state)] < state.cost:
                continue 
            # check if satisfy the requirement 
            if state.nextIdx == n and checkLen(state.strLen) and checkStatus(state.hasLower, state.hasUpper, state.hasDigit):
                return state.cost
    
            # add new char in password 
            if state.nextIdx < n: 
                ch = password[state.nextIdx] 
                addChar(minCost, pq, state, ch, allStates, state.cost, state.nextIdx+1)

                if state.strLen > 6:
                    # delete char in password 
                    delChar(minCost, pq, state, allStates)

                # replace char in password 
                # lower 
                for i in range(ord('a'), ord('z')+1):
                    ch = chr(i)
                    if ch == password[state.nextIdx]:
                        continue
                    if replaceChar(minCost, pq, state, ch, allStates):
                        break 
                # upper 
                for i in range(ord('A'), ord('Z')+1):
                    ch = chr(i)
                    if ch == password[state.nextIdx]:
                        continue
                    if replaceChar(minCost, pq, state, ch, allStates):
                        break 
                # digit 
                for i in range(ord('0'), ord('9')+1):
                    ch = chr(i)
                    if ch == password[state.nextIdx]:
                        continue
                    if replaceChar(minCost, pq, state, ch, allStates):
                        break 

            if state.strLen < 20: 
                # insert new char 
                # lower 
                for i in range(ord('a'), ord('z')+1):
                    ch = chr(i)
                    if addChar(minCost, pq, state, ch, allStates, state.cost+1, state.nextIdx):
                        break 
                # upper 
                for i in range(ord('A'), ord('Z')+1):
                    ch = chr(i)
                    if addChar(minCost, pq, state, ch, allStates, state.cost+1, state.nextIdx):
                        break 
                # digit 
                for i in range(ord('0'), ord('9')+1):
                    ch = chr(i)
                    if addChar(minCost, pq, state, ch, allStates, state.cost+1, state.nextIdx):
                        break 


if __name__ == "__main__": 
    s = Solution()

    password = "a"
    result = s.strongPasswordChecker(password)
    assert result == 5 

    password = "aA1"
    result = s.strongPasswordChecker(password)
    assert result == 3

    password = "1337C0d3"
    result = s.strongPasswordChecker(password)
    assert result == 0

    password = "A"
    result = s.strongPasswordChecker(password)
    assert result == 5 

    password = "aA123"
    result = s.strongPasswordChecker(password)
    assert result == 1 

    password = "aaa111"
    result = s.strongPasswordChecker(password)
    assert result == 2

    password = "aaa"
    result = s.strongPasswordChecker(password)
    assert result == 3

    password = "ABABABABABABABABABAB1"
    result = s.strongPasswordChecker(password)
    assert result == 2