impl Solution {
    fn pre_order(start_idx: i32, n: i32) -> Vec<i32> {
        let mut res = Vec::new(); 
        for i in 0..10 {
            let j = start_idx*10 + i; 
            if i == 0 && j == 0 {
                continue; 
            }
            // base case 
            if j > n {
                return res; 
            }
            // visit 
            res.push(j); 
            // traverse 
            res.extend(Solution::pre_order(j, n));
        }
        res 
    }
    pub fn lexical_order(n: i32) -> Vec<i32> {
        Solution::pre_order(0, n) 
    }
}

struct Solution {}

fn main() {
    assert_eq!(vec![1,10,11,12,13,2,3,4,5,6,7,8,9], Solution::lexical_order(13)); 
}