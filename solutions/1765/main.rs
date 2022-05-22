use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // initialize 
        let row = is_water.len(); 
        let col = is_water[0].len(); 
        let mut ans = is_water.clone(); 
        let mut que = VecDeque::new();
        let dirs: Vec::<(i32, i32)> = vec![(1,0), (-1,0), (0,1), (0,-1)]; 
        // put water cells in queue 
        for i in 0..row {
            for j in 0..col {
                if is_water[i][j] == 1 {
                    ans[i][j] = 0; 
                    que.push_back((i, j)); 
                }
                else {
                    ans[i][j] = -1;
                }
            }
        }
        // bfs 
        let mut h: i32 = 1; 
        while !que.is_empty() {
            let mut q_size = que.len(); 
            while q_size > 0 {
                let (x, y) = que.pop_front().unwrap(); 
                for d in &dirs {
                    let (nx, ny) = ((x as i32+d.0) as usize, (y as i32+d.1) as usize); 
                    if nx >= row || ny >= col {
                        continue; 
                    }
                    if ans[nx][ny] == -1 {
                        ans[nx][ny] = h; 
                        que.push_back((nx, ny)); 
                    }
                }
                q_size -= 1; 
            }
            h += 1; 
        }
        return ans; 
    }
}

fn main() {
    let is_water = vec![vec![0,1], vec![0,0]];
    let result = Solution::highest_peak(is_water);
    println!("{:?}", result);
}
