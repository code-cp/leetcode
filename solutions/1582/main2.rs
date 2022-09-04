impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        // Passed 0ms 2.1mb
        if mat.is_empty() { return 0; }
        let rows = mat.iter().map(|rows| rows.iter().sum()).collect::<Vec<i32>>();
        let cols = (0..mat[0].len()).map(|i| mat.iter().map(|col| col[i]).sum()).collect::<Vec<i32>>();
        (0..mat.len()).fold(0, |acc, i| acc + (0..mat[i].len()).filter(|&j| mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1).count()) as i32
    }
}

// 作者：rui2o2o
// 链接：https://leetcode.cn/problems/special-positions-in-a-binary-matrix/solution/rust-by-ruislan-137/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。