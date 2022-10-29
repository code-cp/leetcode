impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let i = match &rule_key as &str {
            "type" => 0, 
            "color" => 1, 
            "name" => 2, 
            _ => 3, 
        }; 

        items.iter().fold(0, |res, item| res + if item[i] == rule_value {1} else {0})
    }
}