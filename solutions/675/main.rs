use std::collections::VecDeque;
use std::collections::HashSet;
impl Solution {
    pub fn bfs(forest: &Vec<Vec<i32>>, m: usize, n: usize, start: (usize, usize), end: (usize, usize)) -> i32 {
        let dirs = vec![(-1, 0), (0, -1), (1, 0), (0, 1)]; 
        let start = ((start.0, start.1), 0i32); 
        let mut deq = VecDeque::from(vec![start]);
        let mut visited = HashSet::new(); 
        while deq.len() > 0 {
            let (cur, steps) = deq.pop_front().unwrap(); 
            if cur == end {
                return steps; 
            }
            if visited.contains(&cur) {
                continue; 
            }
            visited.insert((cur.0, cur.1));
            for (dx, dy) in dirs.iter() {
                let dx = (cur.0 as i32 + dx) as usize;  
                let dy = (cur.1 as i32 + dy) as usize; 
                if 0 as usize <= dx && dx < m && 0 as usize <= dy && dy < n {
                    if forest[dx][dy] > 0 {
                        deq.push_back(((dx, dy), steps+1));    
                    }
                }
            }
        }
        return -1; 
    }

    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        let m = forest.len(); 
        let n = forest[0].len(); 
        let mut trees: Vec<Vec<usize>> = Vec::new(); 
        for i in 0..m {
            for j in 0..n {
                if forest[i][j] > 1 {
                    trees.push(vec![forest[i][j] as usize, i, j]); 
                }
            }
        }
        trees.sort(); 
        let mut total_steps: i32 = 0; 
        let mut cur = (0, 0); 
        for t in trees {
            let steps = Solution::bfs(&forest, m, n, cur, (t[1], t[2])); 
            cur = (t[1], t[2]); 
            if steps == -1 {
                return -1; 
            }
            total_steps += steps; 
        }
        return total_steps; 
    }
}

struct Solution {}

fn main() {
    let forest: Vec<Vec<i32>> = vec![
        vec![1,2,3],
        vec![0,0,4],
        vec![7,6,5]
    ]; 
    assert_eq!(6, Solution::cut_off_tree(forest));
    
    let forest: Vec<Vec<i32>> = vec![
        vec![1,2,3],
        vec![0,0,0],
        vec![7,6,5]
    ]; 
    assert_eq!(-1, Solution::cut_off_tree(forest));
    
    println!("Pass test cases!"); 
}