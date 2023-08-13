use std::collections::HashSet;
use generate_parentheses::implementations::IMPLEMENTATIONS;

#[test]
fn test_smaller_cases() {
    let cases = [
        (1, to_set(&["()"])),
        (2, to_set(&["(())", "()()"])),
        (3, to_set(&["(())()", "()()()", "()(())", "((()))", "(()())"]))
    ];

    for (n, expected) in cases {
        for (name, gen) in IMPLEMENTATIONS {
            assert_eq!(HashSet::from_iter(gen(n).into_iter()), expected, "We test {} on n={}", name, n);
        }
    }
}

#[test]
fn same_results_on_larger_cases() {
    same_results_on(6);
    same_results_on(7);
}

fn same_results_on(n: i32) {
    let results: Vec<HashSet<String>> = IMPLEMENTATIONS.iter().map(
        |(_, gen)| HashSet::<String>::from_iter(gen(n).into_iter())
    ).collect(); 

    // check results are same for different methods 
    for w in results.windows(2) {
        assert_eq!(w[0], w[1])
    }
}

fn to_set(strs: &[&str]) -> HashSet<String> {
    strs.iter().map(|s| s.to_string()).collect()
}