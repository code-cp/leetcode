// Every valid combination has the following form: (...)... where ... 
// corresponds to a valid combination of a strictly smaller size (including empty string). 
// To enumerate all the combinations, we enumerate all the combinations of smaller sizes and put them into such a form. 
// We should be careful to go other all the sizes without exemption and make sure that the final combination has precisely the size we need.
pub fn generate_parentheses(n: i32) -> Vec<String> {
    // left can be empty, but right cannot be empty 
    let mut combinations: Vec<Vec<String>> = vec![vec!["".to_string()], vec!["()".to_string()]]; 

    for k in 2..=n as usize {
        let mut k_combination = vec![]; 
        for c in 0..k {
            for left in &combinations[c] {
                for right in &combinations[k-1-c] {
                    // valid combinations of size `c + (k-1-c) + 1 = k`
                    k_combination.push(format!("({}){}", left, right)); 
                }
            }
        }
        combinations.push(k_combination); 
    }
    combinations.pop().unwrap()
}