impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let num_sum: i32 = nums.iter().sum();
        let f0 = nums.iter().enumerate().fold(0, |f, (i, &x)| f + i as i32 * x);
        // There is also scan if you need a variation of folding which yeilds the result each time. 
        // This is useful if you're waiting for a certain accumulated amount and wish to check on each iteration.
        f0.max(nums.iter().rev().scan(f0, |f, x| {
            *f = *f + num_sum - nums.len() as i32 * x;
            Some(*f)
        }).max().unwrap())
    }
}

// 作者：934786601
// 链接：https://leetcode-cn.com/problems/rotate-function/solution/by-934786601-ocs0/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

struct Solution {}

fn main() {
    assert_eq!(26, Solution::max_rotate_function(vec![4,3,2,6]));
}