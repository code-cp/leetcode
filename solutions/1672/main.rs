impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        accounts.iter().map(|x| x.iter().sum()).max().unwrap()
    }
}

struct Solution {}

fn main() {
    let accounts = vec![vec![1,2,3], vec![3,2,1]];
    assert_eq!(Solution::maximum_wealth(accounts), 6); 
}