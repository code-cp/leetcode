impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut grid: Vec<Vec<i32>> = vec![vec![1; n as usize]; m as usize]; 
        if m == 1 || n == 1 {
            return grid[0][0]; 
        }

        // last row is all 1 
        // last col is all 1 

        // NOTE, use rev in rust, it cannot go backward 
        // NOTE, when m = 1, m as usize - 2 will overflow 
        for i in (0..=(m as usize-2)).rev() {
            for j in (0..=(n as usize-2)).rev() {
                // cur = down + right 
                grid[i][j] = grid[i+1][j] + grid[i][j+1]; 
            }
        }
        grid[0][0]
    }
}