impl Solution {
    pub fn backtrack(matchsticks: &Vec<i32>, target: i32, sides: &mut Vec<i32>, i: usize) -> bool {
        // base case 
        if i == matchsticks.len() {
            return true;
        }

        // recursive case 
        for j in 0..4 {
            if j > 0 && sides[j - 1] == sides[j] {
                continue;
            }
            if sides[j] + matchsticks[i] <= target {
                sides[j] += matchsticks[i];
                if Solution::backtrack(&matchsticks, target, sides, i + 1) {
                    return true;
                }
                sides[j] -= matchsticks[i];
            }
        }

        return false; 
    }
    pub fn makesquare(matchsticks: Vec<i32>) -> bool {
        let sum = matchsticks.iter().sum::<i32>();
        if sum % 4 != 0 {
            return false;
        }
        let mut matchsticks = matchsticks.clone(); 
        matchsticks.sort(); 
        matchsticks.reverse(); 
        let target = sum / 4; 
        let mut sides = vec![0; 4]; 
        Self::backtrack(&matchsticks, target, &mut sides, 0)
    }
}

struct Solution {}

fn main() {
    assert_eq!(true, Solution::makesquare(vec![1,1,2,2,2]));
}