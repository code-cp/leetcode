from typing import * 

        # 背包
        # 不直接考虑选哪几个物体
        # 考虑装满1kg物品的value，2kg物品的value。。。
        # for object: 
            # for capacity
                # dp[capacity] = dp[capacity-cap[i]] + val[i]
                # 或者
                # dp[capacity+cap[i]] = dp[capacity] + val[i]
                # 注意capacity+cap[i]是加号 
        
        # 背包的最大特点是从skillset角度考虑
        # 而不是从选哪个人考虑
        # ie解空间是skillset
        # for people 
            # for skillset 
                # new skillset = skillset + skill[i]
                # dp[new skillset] = min(dp[new skillset], dp[skillset] + 1) 
        # return dp[required skillset]
        
        # 注意传统背包写法是
        # old skillset = cur skillset - skill[i] 
        # 但是cur skillset = old skillset | skill[i]，逆运算不好求

        # 在某个范围内选择，比如在物品中选择，或者人中选择，是背包问题的特征

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        res = {}
        
        # people to skill 
        # 状态压缩
        skill2num = {}
        for i, s in enumerate(req_skills): 
            skill2num[s] = i 
        p2s = [0]*len(people)
        for i in range(len(people)):
            skillset = 0 
            for skill in people[i]: 
                if skill not in skill2num: 
                    continue 
                idx = skill2num[skill]
                skillset += (1<<idx)
            p2s[i] = skillset 
                
        dp = [float("inf")]*(1<<n)
        # 如果是0个skill，需要0个人，其他情况都需要更新，初始值都是无穷大
        # dp[0]不会作为一个new skill出现
        dp[0] = 0 
        for i in range(len(people)): 
            # dp是上一轮的状态,dp2是这一轮的状态
            dp2 = [i for i in dp]    
            for skillset in range(1<<n):
                new_skillset = skillset | p2s[i]
                new_p = dp[skillset]+1
                if new_p < dp2[new_skillset]:
                    dp2[new_skillset] = new_p
                    res[new_skillset] = res.get(skillset, [])+[i]
            dp = [i for i in dp2]
        
        return res[(1<<n)-1]
    
if __name__ == "__main__": 
    s = Solution() 
    
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    assert s.smallestSufficientTeam(req_skills, people) == [0,2]