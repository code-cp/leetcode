impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        fn gcd(m: i32, n: i32) -> i32 {
            let mut a = m; 
            let mut b = n; 
            while b > 0 {
                let temp = a; 
                a = b; 
                b = temp % b; 
            }
            a as i32 
        }

        let n = nums.len(); 
        let mut gcd_results = vec![vec![0; n]; n]; 
        
        for i in 0..n {
            for j in i+1..n {
                gcd_results[i][j] = gcd(nums[i], nums[j]); 
            }
        }

        fn dfs(n: usize, opt: i32, mask: i32, gcd_results: &Vec<Vec<i32>>, memo: &mut Vec<i32>) -> i32 {
            let mut ans = 0; 
            // base case 
            if mask == (1<<n-1) {
                return ans; 
            }
            ans = memo[mask as usize]; 
            if ans > 0 {
                return ans; 
            }
            // recursion 
            // mask 0: unused, 1: used
            for i in 0..n {
                if mask & (1<<i) == 0 {
                    for j in i+1..n {
                        if mask & (1<<j) == 0 {
                            ans = ans.max(opt*gcd_results[i][j] + 
                                dfs(n, opt+1, mask | (1<<i) | (1<<j), &gcd_results, memo));
                            memo[mask as usize] = ans;
                        }
                    }
                }
            }
            return ans; 
        }
        
        let mut memo = vec![0; 1<<n]; 
        dfs(n, 1, 0, &gcd_results, &mut memo); 
        memo[0]
    }
}

struct Solution {}

fn main() {
    let nums = vec![3,4,6,8]; 
    assert_eq!(Solution::max_score(nums), 11); 
}