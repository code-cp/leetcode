impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut record = vec![0; 26]; 
        for ch in ransom_note.bytes() {
            record[ch as usize - 'a' as usize] -= 1; 
        }
        for ch in magazine.bytes() {
            record[ch as usize - 'a' as usize] += 1;  
        }
        for r in record.iter() {
            if *r < 0 {
                return false; 
            }
        }
        true 
    }
}