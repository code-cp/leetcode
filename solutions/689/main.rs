use std::cmp::Reverse;

// struct Solution; 

impl Solution {
    pub fn max_sum_of_three_subarrays(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let (n, k) = (nums.len(), k as usize); 
        let mut sum = Vec::with_capacity(n-k+1); 
        // 先求前k个数的和
        sum.push(nums.iter().take(k).fold(0, |acc, &x| acc + x as i64)); 
        // 继续求后面的和
        for i in 0..n-k {
            sum.push(*sum.last().unwrap() - nums[i] as i64 + nums[i+k] as i64);  
        }

        // 求前缀中和最大的k个数的区间，l后面至少有2*k个数
        let l = n-k*3+1; 
        let mut pref = Vec::with_capacity(l); 
        pref.push(0); 
        for i in 1..l {
            let j = *pref.last().unwrap(); 
            pref.push(if sum[i] > sum[j] {i} else {j}); 
        }

        let mut suff = Vec::with_capacity(l); 
        suff.push(n-k); 
        for i in (n-k-l+1..n-k).rev() {
            let j = *suff.last().unwrap(); 
            suff.push(if sum[i] >= sum[j] {i} else {j}); 
        }

        // 滑动中间的区间，b的范围是k到n-k*2 
        // a从b-k的前缀中选,c从n-k*2-b的后缀中选
        let (a, b, c) = (k..=n-k*2).map(
            |b| {
                let (a, c) = (pref[b-k], suff[n-k*2-b]); 
                (sum[a] + sum[b] + sum[c], Reverse((a, b, c)))
            }
        ).max().unwrap().1.0; 

        vec![a as i32, b as i32, c as i32]
    }
}

// fn main() {
//     assert_eq!(Solution::max_sum_of_three_subarrays(vec![1,2,1,2,6,7,5,1], 2), vec![0,3,5]);
// }