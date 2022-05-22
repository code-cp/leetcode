use std::collections::{HashSet, HashMap}; 

struct Solution {}

impl Solution {
    pub fn grid_illumination(n: i32, lamps: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut lamps_set = HashSet::new(); 
        let mut row_count = HashMap::new(); 
        let mut col_count = HashMap::new(); 
        let mut diag_count = HashMap::new();
        let mut bdiag_count = HashMap::new(); 
        
        for l in lamps {
            lamps_set.insert((l[0], l[1])); 
        }
        for l in &lamps_set {
            *row_count.entry(l.0).or_insert(0) += 1; 
            *col_count.entry(l.1).or_insert(0) += 1; 
            *diag_count.entry(l.0-l.1).or_insert(0) += 1; 
            *bdiag_count.entry(l.0+l.1).or_insert(0) += 1; 
        }
        
        let mut ans = Vec::new(); 
        for q in &queries {
            if *row_count.entry(q[0]).or_insert(0) > 0 || *col_count.entry(q[1]).or_insert(0) > 0 || *diag_count.entry(q[0]-q[1]).or_insert(0) > 0 || *bdiag_count.entry(q[0]+q[1]).or_insert(0) > 0 {
                ans.push(1); 
            }
            else {
                ans.push(0); 
            }

            for dx in -1..2 {
                for dy in -1..2 {
                    let x = &dx+&q[0]; 
                    let y = &dy+&q[1]; 
                    if x < 0 || x > n-1 || y < 0 || y > n-1 {
                        continue; 
                    }
                    if lamps_set.contains(&(x, y)) {
                        lamps_set.remove(&(x, y)); 
                        *(row_count.get_mut(&x).unwrap()) -= 1; 
                        *(col_count.get_mut(&y).unwrap()) -= 1; 
                        *(diag_count.get_mut(&(x-y)).unwrap()) -= 1; 
                        *(bdiag_count.get_mut(&(x+y)).unwrap()) -= 1; 
                    }
                }
            }
        }
        return ans; 
    }
}

fn main() {
    let n = 5; 
    assert_eq!(Solution::grid_illumination(n, vec![vec![0,0], vec![4,4]], vec![vec![1,1], vec![1,0]]), vec![1,0]); 
}