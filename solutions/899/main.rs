impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        let mut v = s.chars().collect::<Vec<char>>(); 
        let n = v.len(); 

        if k == 1 {
            // ref https://doc.rust-lang.org/std/vec/struct.Vec.html#method.extend_from_within
            v.extend_from_within(0..); 
            let mut ans = &v[0..n]; 

            for i in 1..n {
                if ans > &v[i..n+i] {
                    ans = &v[i..n+i]; 
                }
            }

            ans.into_iter().collect()
        } else {
            v.sort(); 
            v.into_iter().collect()
        }
    }
}