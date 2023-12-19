// struct Solution; 

impl Solution {
    /// https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=38f09d1409cc168703cd209c06872c2f
    fn calculate_presum(arr: &Vec<i32>) -> Vec<i32> {
        let mut presum = Vec::with_capacity(arr.len());

        // let a = [1, 2, 3];

        // let mut iter = a.iter().scan(1, |state, &x| {
        //     // each iteration, we'll multiply the state by the element
        //     *state = *state * x;
        
        //     // then, we'll yield the negation of the state
        //     Some(-*state)
        // });
        
        // assert_eq!(iter.next(), Some(-1));
        // assert_eq!(iter.next(), Some(-2));
        // assert_eq!(iter.next(), Some(-6));
        // assert_eq!(iter.next(), None);
        let sum_iter = arr.iter().scan(
            0, |state, &x| {
                *state += x; 
                Some(*state)
            }
        ); 

        // take: An iterator that only iterates over the first n iterations of iter
        presum.extend(sum_iter.take(arr.len())); 

        // 前边补一个0，方便计算
        presum.insert(0, 0);

        presum 
    }
    pub fn max_sum_of_three_subarrays(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let presum = Self::calculate_presum(&nums);
        let (n, k) = (nums.len(), k as usize);

        // 记录左边滑动窗口里，最大前缀
        let mut left_max = vec![0; n];
        let mut left_idices = vec![0; n];
        let mut max_sum = 0;
        let mut max_idx = 0;  
        for i in k-1..n {
            let sum = presum[i+1] - presum[i+1-k];
            if sum > max_sum {
                max_sum = sum; 
                // 记录的是滑动窗口的左端点
                // 注意不能用i-k+1，会overflow
                max_idx = i+1-k; 
            }
            left_max[i] = max_sum; 
            left_idices[i] = max_idx; 
        }

        // 记录右边滑动窗口里，最大后缀
        let mut right_max = vec![0; n];
        let mut right_indices = vec![0; n]; 
        let mut max_sum = 0; 
        let mut max_idx = 0; 
        for i in (0..=n-k).rev() {
            // i到i+k-1
            let sum = presum[i+k] - presum[i]; 
            // 注意是>=，不是>
            if sum >= max_sum {
                max_sum = sum;
                // 记录左端点 
                max_idx = i; 
            } 
            right_max[i] = max_sum; 
            right_indices[i] = max_idx; 
        }

        // 遍历中间的区间
        // 左边至少有k个数，右边至少有k个数
        // 所以左边至少是[0,k-1]，右边至少是[n-k+1,n-1]
        let mut res = 0;
        let mut idx = Vec::with_capacity(3);  
        for i in k..=n-k*2 {
            // i到i+k-1
            let sum = presum[i+k] - presum[i]; 
            if sum+left_max[i-1]+right_max[i+k] > res {
                res = sum+left_max[i-1]+right_max[i+k];  
                idx = vec![left_idices[i-1] as i32, i as i32, right_indices[i+k] as i32]; 
            }
        }

        idx 
    }
}

// fn main() {
//     assert_eq!(Solution::max_sum_of_three_subarrays(vec![1,2,1,2,6,7,5,1], 2), vec![0,3,5]);
// }