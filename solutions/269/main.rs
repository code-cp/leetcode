// 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

// 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

// 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

// 字符串 s 字典顺序小于 字符串 t 有两种情况：

// 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
// 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
//  

// 示例 1：

// 输入：words = ["wrt","wrf","er","ett","rftt"]
// 输出："wertf"
// 示例 2：

// 输入：words = ["z","x"]
// 输出："zx"
// 示例 3：

// 输入：words = ["z","x","z"]
// 输出：""
// 解释：不存在合法字母顺序，因此返回 "" 。

// 注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/

// 来源：力扣（LeetCode）
// 链接：https://leetcode.cn/problems/Jf1JuT
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

use std::collections::HashMap; 
#[derive(Clone, PartialEq, Debug)]
enum Status {
    SEARCHING,
    SEARCHED,
}
impl Solution {
    pub fn dfs(adj: &HashMap<char, Vec<char>>, visited: &mut HashMap<char, Status>, stack: &mut Vec<char>, cur: char) -> bool {
        if visited.contains_key(&cur) {
            return *visited.get(&cur).unwrap() != Status::SEARCHING;
        }
        *visited.entry(cur).or_insert(Status::SEARCHING) = Status::SEARCHING;
        for next in adj.get(&cur).unwrap_or(&vec![]).iter() {
            if !Solution::dfs(adj, visited, stack, *next) {
                return false; 
            }
        }
        *visited.entry(cur).or_insert(Status::SEARCHED) = Status::SEARCHED;
        stack.push(cur);
        return true; 
    }
    pub fn alien_order(words: Vec<String>) -> String {
        // init adjacency list 
        let mut adj = HashMap::new(); 
        words.iter().for_each(|word| {
            for c in word.chars() {
                adj.entry(c).or_insert(vec![]);
            }
        });
        // build adjacency list 
        for i in 0..words.len()-1 {
            let word1 = words[i].chars().collect::<Vec<char>>();
            let word2 = words[i+1].chars().collect::<Vec<char>>();
            let mut j = 0;
            for (c1, c2) in word1.iter().zip(word2.iter()) {
                if c1 != c2 {
                    adj.get_mut(c1).unwrap().push(*c2);
                    break;
                }
                j += 1;
            }
            // check violation 
            if j == word2.len() && word1.len() > word2.len() {
                return "".to_string();
            }
        } 
        // dfs 
        let mut visited = HashMap::new();
        let mut stack = vec![];
        for c in adj.keys() {
            if !Solution::dfs(&adj, &mut visited, &mut stack, *c) {
                return "".to_string();
            }
        }
        stack.iter().rev().map(|c| c.to_string()).collect::<Vec<String>>().join("")
    }
}

struct Solution {}

fn main() {
    let words = vec!["wrt".to_string(),"wrf".to_string(),"er".to_string(),"ett".to_string(),"rftt".to_string()]; 
    assert_eq!("wertf".to_string(), Solution::alien_order(words));
}