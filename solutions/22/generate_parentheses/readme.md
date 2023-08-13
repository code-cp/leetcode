## how to run 

```shell
(base) ➜  generate_parentheses git:(main) ✗ cargo run -- -v -s 12 bfs 
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/generate_parentheses -v -s 12 bfs`
== Running bfs ==
Got results in: 55.30ms
Resulting vector info:
  Size: 208012
  Capacity: 208012
  Total Strings' Capacity: 7.6 MB
  Average Capacity per String: 38
  Total memory used: 12.3 MB
```

## reference

- https://github.com/bravit/generate_parentheses/tree/master
- https://gist.github.com/KodrAus/97c92c07a90b1fdd6853654357fd557a
- https://doc.rust-lang.org/rust-by-example/mod/split.html

- https://www.youtube.com/watch?v=JRMOIE_wAFk&ab_channel=Rust
- https://www.justanotherdot.com/posts/profiling-with-perf-and-dhat-on-rust-code-in-linux.html
- https://www.reddit.com/r/rust/comments/rxj81f/rust_profiling/