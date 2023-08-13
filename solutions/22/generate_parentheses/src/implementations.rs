pub mod dfs;
pub mod bfs;
pub mod sub;

pub type GenerateParenthesesFn = fn(i32) -> Vec<String>;

pub static IMPLEMENTATIONS: &[(&str, GenerateParenthesesFn)] = &[
    ("dfs", dfs::generate_parentheses),
    ("bfs", bfs::generate_parentheses),
    ("sub", sub::generate_parentheses),
]; 

pub fn find_implementation(impl_name: &str) -> Option<GenerateParenthesesFn> {
    IMPLEMENTATIONS.iter().find(
        |(name, _)| impl_name == *name  
    ).map(|(_, fun)| *fun) 
}