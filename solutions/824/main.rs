impl Solution {
    pub fn to_goat_latin(sentence: String) -> String {
        sentence
            .split_ascii_whitespace()
            .enumerate()
            .map(
                |(i, s)| match s[..1].to_lowercase().starts_with(&['a', 'e', 'i', 'o', 'u'][..]) {
                    true => s.to_string() + "ma" + "a".repeat(i + 1).as_str(),
                    false => s[1..].to_string() + &s[0..1] + "ma" + "a".repeat(i + 1).as_str(),
                },
            )
            .collect::<Vec<_>>()
            .join(" ")
    }
}

struct Solution {}

fn main() {
    assert_eq!(
        Solution::to_goat_latin("I speak Goat Latin".to_string()),
        "Imaa peaksmaaa oatGmaaaa atinLmaaaaa".to_string()
    );
    assert_eq!(
        Solution::to_goat_latin("The quick brown fox jumped over the lazy dog".to_string()),
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa".to_string()
    );
}