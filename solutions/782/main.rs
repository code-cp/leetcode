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
    pub fn moves_to_chessboard(board: Vec<Vec<i32>>) -> i32 {
        let n = board.len();
        
        for r in 0..n {
            for c in 0..n {
                if (board[0][0] ^ board[r][0] ^ board[r][c] ^ board[0][c]) == 1 {
                    return -1; 
                }
            }
        }

        let add_i = |i, x| {
            if x as usize == i % 2 {
                return 1; 
            } else {
                return 0; 
            }
        };

        let (mut rowSum, mut colSum, mut rowSwap, mut colSwap) = (0, 0, 0, 0); 
        let rowSum = Index::index(&board, 0).iter().fold(0, |acc, x| acc + x); 
        let mut rowSwap = board[0].clone().into_iter().enumerate().fold(0, |acc, (i, x)| acc + add_i(i, x)); 
        let board_T = transpose(board); 
        let colSum = Index::index(&board_T, 0).iter().fold(0, |acc, x| acc + x);
        let mut colSwap = board_T[0].clone().into_iter().enumerate().fold(0, |acc, (i, x)| acc + add_i(i, x)); 
        
        if rowSum as usize != n/2 && rowSum as usize != (n+1)/2 {
            return -1; 
        }
        if colSum as usize != n/2 && colSum as usize != (n+1)/2 {
            return -1; 
        }

        if n % 2 == 1{
            if rowSwap % 2 == 1 {
                rowSwap = n - rowSwap; 
            }
            if colSwap % 2 == 1 {
                colSwap = n - colSwap; 
            }
        }
        else {
            colSwap = colSwap.min(n - colSwap);
            rowSwap = rowSwap.min(n - rowSwap);
        }
        ((rowSwap as i32 + colSwap as i32) / 2) 
    }
}