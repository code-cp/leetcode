pub fn dfs(cur: &mut String, open: usize, close: usize, ans: &mut Vec<String>) {
    // base case 
    if open == 0 && close == 0 {
        ans.push(cur.clone()); 
        return; 
    }
    if open > 0 {
        cur.push('(');
        dfs(cur, open-1, close+1, ans);  
        cur.pop(); 
    }
    if close > 0 {
        cur.push(')'); 
        dfs(cur, open, close-1, ans); 
        cur.pop(); 
    }
}

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut ans = vec![];
        let mut cur = String::new();  
        dfs(&mut cur, n as usize, 0, &mut ans); 
        ans 
    }
}