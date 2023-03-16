from typing import * 

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        train_energy = -initialEnergy
        train_energy += sum(energy)+1 
        train_experience = 0
        cur_exp = initialExperience
        for e in experience: 
            if cur_exp <= e: 
                train_experience += e-cur_exp+1
                cur_exp = e+1
            cur_exp += e 
        res = max(train_energy, 0) + train_experience
        return res 
    
    
if __name__ == "__main__": 
    s = Solution() 

    initialEnergy = 1
    initialExperience = 1
    energy = [1,1,1,1]
    experience = [1,1,1,50]
    assert s.minNumberOfHours(initialEnergy, initialExperience, energy, experience) == 51
    
    # initialEnergy = 5
    # initialExperience = 3
    # energy = [1,4,3,2]
    # experience = [2,6,3,1]
    # assert s.minNumberOfHours(initialEnergy, initialExperience, energy, experience) == 8
        