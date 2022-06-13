impl Solution {
    pub fn state_to_time(jobs: &[i32], state: i32) -> i32 {
        let mut state = state; 
        let mut time = 0;
        let mut count = 0; 
        while state > 0 {
            if state & 1 == 1 {
                time += jobs[count];
            } 
            state >>= 1; 
            count += 1; 
        }
        time 
    }
    pub fn minimum_time_required(jobs: Vec<i32>, k: i32) -> i32 {
        // dp able 
        let n = jobs.len(); 
        let mut dp = vec![vec![0; (2 as i32).pow(n as u32) as usize]; k as usize];
        // init dp 
        for i in 0..(2 as i32).pow(n as u32) {
            dp[0][i as usize] = Solution::state_to_time(&jobs.as_slice(), i);
        } 
        // traverse 
        for i in 1..k {
            for state in 0..(2 as i32).pow(n as u32) {
                let mut min = std::i32::MAX;
                let mut subset = state; 
                while subset > 0 {
                    min = min.min(dp[i as usize - 1][(state ^ subset) as usize].max(dp[0][subset as usize])); 
                    subset = (subset - 1) & state; 
                }
                dp[i as usize][state as usize] = min; 
            }
        }
        dp[dp.len()-1][dp[0].len()-1]
    }
}

struct Solution {}

fn main() {
    assert_eq!(Solution::minimum_time_required(vec![3,2,3], 3), 3); 
}