fn main() {
    assert_eq!(Solution::find_min_difference(vec!["23:59".to_string(),"00:00".to_string()]), 1); 
}

struct Solution {}

impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let mut time_set = std::collections::HashSet::new();
        let str_to_time = |s: &[u8]| (s[0] as i32 * 10 + s[1] as i32);
        for t in time_points.into_iter() {
            let c = t.as_bytes();
            let k = str_to_time(&c[0..2]) * 60 + str_to_time(&c[3..]);
            if time_set.contains(&k) {
                return 0;
            }
            time_set.insert(k);
        }
        let mut diff: Vec<_> = time_set.into_iter().collect();
        diff.sort();
        diff.push(diff[0] + 24*60);
        (1..diff.len()).map(|i| diff[i] - diff[i-1]).min().unwrap()
    }
}
