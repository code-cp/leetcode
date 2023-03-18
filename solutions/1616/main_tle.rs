struct Solution {}

impl Solution {
    pub fn check_pal(a: String, b: String) -> bool {
        let check_pal = |p: &str| p == p.chars().rev().collect::<String>();

        if check_pal(&a) || check_pal(&b) {
            return true;
        }

        let n = a.len();
        // NOTE, cannot build hashmap, will tle 
        // when str len is very large, may have lots of hash collision 
        let mut suf_b_map = std::collections::HashMap::new();

        for i in 0..n {
            suf_b_map.insert(b[i..].chars().rev().collect::<String>(), i);
        }

        for i in 0..n {
            let pre_a = &a[..=i];
            let j = *suf_b_map.get(pre_a).unwrap_or(&0);

            if j == 0 {
                continue;
            }

            if check_pal(&a[i+1..j]) || check_pal(&b[i+1..j]) {
                return true;
            }
        }

        false 
    }
    pub fn check_palindrome_formation(a: String, b: String) -> bool {
        Solution::check_pal(a.clone(), b.clone()) || Solution::check_pal(b, a)
    }
}
