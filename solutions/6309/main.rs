struct Solution {}

impl Solution {
    fn find_valid_split(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut first_pos = std::collections::HashMap::new();
        // right most position for i is at least i 
        let mut right_pos = (0..n).collect::<Vec<usize>>();
        
        fn update(p: i32, i: usize, first_pos: &mut std::collections::HashMap<i32, usize>, right_pos: &mut Vec<usize>) {
            if !first_pos.contains_key(&p) { 
                // first time p appears 
                first_pos.insert(p, i);
            } else {  
                right_pos[*first_pos.get(&p).unwrap()] = i;
            }
        }
        
        for (i, x) in nums.iter().enumerate() { 
            let mut fac = 2; 
            let mut x = *x;
            while fac * fac <= x { 
                if x % fac == 0 { 
                    update(fac, i, &mut first_pos, &mut right_pos);
                    while x % fac == 0 { 
                        x /= fac; 
                    } 
                } 
                fac += 1; 
            } 
            if x > 1 { 
                update(x, i, &mut first_pos, &mut right_pos);
            }
        }
        
        let mut i = 0; 
        let mut right = 0; 
        // exit while loop when i > right 
        while i <= right { 
            right = std::cmp::max(right, right_pos[i]);
            i += 1;             
        }
        
        if right < n - 1 {
            return right as i32;
        } else {
            return -1;
        }
    }
}