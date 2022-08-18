// ref https://leetcode.cn/problems/maximum-equal-frequency/solution/rust-by-drackramoray-pm32/

use std::collections::HashMap;
impl Solution {
    pub fn max_equal_freq(nums: Vec<i32>) -> i32 {
        let n = nums.len(); 
        let mut ans = 0; 
        let mut cnt: HashMap<i32, i32> = HashMap::new(); 
        let mut freq: HashMap<i32, i32> = HashMap::new(); 

        for i in 1..=n {
            let mut c = cnt.entry(nums[i-1]).or_default(); 
            *freq.entry(*c).or_default() -= 1; 
            *c += 1; 
            let v = *c; 
            cnt.insert(nums[i-1], v); 
            *freq.entry(v).or_default() += 1; 

            // 如果现在所有数频率相等，那么去掉下一个就行
            if *freq.entry(v).or_default() * v == i as i32 && i < n {
                ans = i as i32 + 1; 
            }

            let d = i as i32 - (*freq.entry(v).or_default()) * v; 
            
            // 除掉出现次数为v的数，剩下的数如果出现次数为1，或者v+1，那么去掉这个数可以满足条件
            if (d == v+1 || d==1) && *freq.entry(d).or_default() == 1 {
                ans = i as i32; 
            }
        }

        ans 
    }
}