use std::ops::Index;

// ref https://stackoverflow.com/a/64499219/8519188
fn transpose<T>(v: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!v.is_empty());
    let len = v[0].len();
    let mut iters: Vec<_> = v.into_iter().map(|n| n.into_iter()).collect();
    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap())
                .collect::<Vec<T>>()
        })
        .collect()
}

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len(); 
        let n = mat[0].len(); 
        let mut rowSums = vec![0; m];
        let mut colSums = vec![0; n];
        for i in 0..m {
            let rowSum = Index::index(&mat, i).iter().fold(0, |acc, x| acc + x);
            rowSums[i] = rowSum; 
        }
        let mat = transpose(mat); 
        for i in 0..n {
            let colSum = Index::index(&mat, i).iter().fold(0, |acc, x| acc + x);
            colSums[i] = colSum; 
        }
        let mat = transpose(mat); 
        let mut cnt = 0; 
        for r in 0..m {
            for c in 0..n {
                if mat[r][c] == 1 && rowSums[r] == 1 && colSums[c] == 1 {
                    cnt += 1; 
                }
            }
        }
        cnt
    }
}
