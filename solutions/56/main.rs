impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        let mut intervals = intervals.clone();  
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut left = intervals[0][0];
        let mut right = intervals[0][1]; 
        for interval in intervals.into_iter().skip(1) {
            if right >= interval[0] {
                right = right.max(interval[1]);
            } else {
                ans.push(vec![left, right]);
                left = interval[0]; 
                right = interval[1]; 
            }
        }
        // NOTE, don't forget to push the last interval 
        ans.push(vec![left, right]);
        ans 
    }
}