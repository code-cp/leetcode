impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut indegrees = vec![0; num_courses as usize]; 
        let mut edges = vec![vec![]; num_courses as usize]; 
        for v in prerequisites.iter() {
            indegrees[v[0] as usize] += 1; 
            edges[v[1] as usize].push(v[0] as usize); 
        }

        let mut ans: Vec<usize> = (0..num_courses as usize).filter(|&i| indegrees[i] == 0).collect();
        let mut i = 0; 
        while i < ans.len() {
            for &j in edges[ans[i]].iter() {
                indegrees[j] -= 1; 
                if indegrees[j] == 0 {
                    ans.push(j); 
                }
            }
            i += 1; 
        }
        match ans.len() < num_courses as usize {
            true => vec![], 
            _ => ans.iter().map(|&i| i as i32).collect()
        }
    }
}