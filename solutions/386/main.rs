impl Solution {
    fn pre_order(start_idx: i32, n: i32) -> Vec<i32> {
        let mut res = Vec::new(); 
        for i in 0..10 {
            let j = start_idx*10 + i; 
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
        let mut res = Vec::new(); 
        if n < 10 {
            for i in 1..(n+1) {
                res.push(i); 
            }
            return res; 
        }
        for i in 1..10 {
            // visit 
            res.push(i); 
            // traverse 
            res.extend(Solution::pre_order(i, n)); 
        }
        res 
    }
}

struct Solution {}

fn main() {
    assert_eq!(vec![1,10,11,12,13,2,3,4,5,6,7,8,9], Solution::lexical_order(13)); 
}