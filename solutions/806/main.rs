// ref https://leetcode-cn.com/problems/number-of-lines-to-write-string/solution/rustgojava-mo-ni-100-by-kyushu-eh70/

impl Solution {
    pub fn number_of_lines(widths: Vec<i32>, s: String) -> Vec<i32> {
        s.bytes().fold(vec![1, 0], |(mut ret), ch| {
            let wid = widths[(ch - 'a' as u8) as usize]; 
            ret[1] += wid;
            if ret[1] > 100 { vec![ret[0] + 1, wid] } else { ret }
        })
    }
}

struct Solution {}

fn main() {
    let widths = vec![10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10];
    let S = "abcdefghijklmnopqrstuvwxyz".to_string(); 
    let ret = Solution::number_of_lines(widths, S); 
    assert_eq!(ret, vec![3, 60]); 
}