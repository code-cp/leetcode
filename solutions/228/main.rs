const CONNECTOR: &str = "->"; 

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let n = nums.len(); 
        let mut result = Vec::new(); 

        if n == 0 {
            return result; 
        }

        let (mut start, mut end) = (0_usize, 0_usize);
        while end <= n {
            if end == n || (end - start) as i32 != nums[end] - nums[start] {
                let s = if start + 1 == end {
                    nums[start].to_string()   
                } else {
                    nums[start].to_string() + CONNECTOR + &nums[end-1].to_string()
                }; 
                result.push(s); 
                start = end; 
            }

            end += 1; 
        }

        result 
    }
}