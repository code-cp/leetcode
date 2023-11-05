impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        if s.len() < 10 {
            return vec![]; 
        }

        let chars = s.chars().collect::<Vec<_>>(); 
        let idx = |c: char| -> i32 {
            match c {
                'A' => 0,
                'C' => 1,
                'G' => 2,
                'T' => 3,
                _ => 0,
            }
        }; 

        let mut ans = vec![]; 
        // usize: The size of this primitive is how many bytes it takes to reference any location in memory. For example, on a 32 bit target, this is 4 bytes and on a 64 bit target, this is 8 bytes.
        let mut count = vec![0_i8; 4_i32.pow(10) as usize]; 
        let mut state = chars[0..10].iter().fold(
            0, |acc, &c| {
                acc * 4 + idx(c) 
            }
        ); 
        count[state as usize] = 1; 

        for i in 10..chars.len() {
            // remove the highest bit and add the new char 
            state = (state - idx(chars[i-10]) * 4_i32.pow(9)) * 4 + idx(chars[i]);
            if count[state as usize] == 1 {
                ans.push(chars[i-9..=i].iter().collect::<String>()); 
                count[state as usize] += 1; 
            } else if count[state as usize] == 0 {
                count[state as usize] = 1; 
            }
        } 

        return ans; 
    }
}