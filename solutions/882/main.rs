use std::cmp::{Ord, Ordering}; 
use std::collections::HashMap;
use std::collections::hash_map::Entry;
// This will be a max-heap
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq, Clone, Debug)]
enum EdgeWeight {
    Infinite, 
    Number(usize), 
}

// The priority queue depends on `Ord`.
// Explicitly implement the trait so the queue becomes a min-heap
// instead of a max-heap.
impl Ord for EdgeWeight {
    fn cmp(&self, other: &EdgeWeight) -> Ordering {
        match other {
            EdgeWeight::Infinite => match self {
                EdgeWeight::Infinite => Ordering::Equal, 
                _ => Ordering::Greater, 
            },
            EdgeWeight::Number(n1) => match self {
                EdgeWeight::Infinite => Ordering::Less, 
                EdgeWeight::Number(n2) => n1.cmp(n2), 
            }
        }
    }
}

// `PartialOrd` needs to be implemented as well.
impl PartialOrd for EdgeWeight {
    fn partial_cmp(&self, other: &EdgeWeight) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct Edge {
    weight: usize, 
    node: usize, 
}

struct Graph {
    adjacency_list: HashMap<usize, Vec<Edge>>, 
    num_nodes: usize, 
}

impl Graph {
    fn new(n: i32) -> Graph {
        Graph {
            adjacency_list: HashMap::<usize, Vec<Edge>>::new(), 
            num_nodes: n as usize, 
        }
    }

    fn set_edges(&mut self, edges: &Vec<Vec<i32>>) {
        for e in edges.into_iter() {
            let n1 = e[0] as usize; 
            let n2 = e[1] as usize; 
            let w = (e[2]+1) as usize;  
            let edge = Edge {
                weight: w, 
                node: n2,
            };
            match self.adjacency_list.entry(n1) {
                Entry::Vacant(e) => { e.insert(vec![edge]); },
                Entry::Occupied(mut e) => { e.get_mut().push(edge); }
            }; 
            let edge = Edge {
                weight: w, 
                node: n1,
            };
            match self.adjacency_list.entry(n2) {
                Entry::Vacant(e) => { e.insert(vec![edge]); },
                Entry::Occupied(mut e) => { e.get_mut().push(edge); }
            };  
        }        
    }

    fn shortest_path(&self) -> Vec<EdgeWeight> {
        let mut pq = BinaryHeap::new();  
        pq.push((EdgeWeight::Number(0), 0));
        let mut dist: Vec<EdgeWeight> = vec![EdgeWeight::Infinite; self.num_nodes]; 
        let mut visited: Vec<i32> = vec![0; self.num_nodes]; 

        // check if node 0 in adj list 
        if !self.adjacency_list.contains_key(&0) {
            return dist; 
        }

        while let Some((w, v)) = pq.pop() {
            if visited[v] == 1 {
                continue; 
            }
            visited[v] = 1; 
            dist[v] = w.clone(); 
            for e in &self.adjacency_list[&v] {
                let new_dist = match w {
                    EdgeWeight::Number(n) => EdgeWeight::Number(n + e.weight), 
                    _ => EdgeWeight::Infinite, 
                }; 
                pq.push((new_dist, e.node));
            }
        }

        return dist; 
    } 
}

struct Solution {}

impl Solution {
    pub fn reachable_nodes(edges: Vec<Vec<i32>>, max_moves: i32, n: i32) -> i32 {
        let mut graph = Graph::new(n);
        graph.set_edges(&edges); 
        let dist = graph.shortest_path(); 
        let max_moves = max_moves as usize;
        let mut ans = 0; 
        for d in &dist {
            match d {
                EdgeWeight::Number(n) => {
                    if n <= &max_moves {
                        ans += 1; 
                    }
                }, 
                _ => {}, 
            }; 
        }
        for (u,v,cnt) in edges.into_iter().map(|e| (e[0] as usize, e[1] as usize, e[2] as usize)) {
            match dist[u] {
                EdgeWeight::Number(n1) => {
                    match dist[v] {
                        EdgeWeight::Number(n2) => {
                            ans += cnt.min(max_moves.saturating_sub(n1) + max_moves.saturating_sub(n2));
                        }, 
                        _ => {}, 
                    }; 
                }, 
                _ => {}, 
            }; 
        }
        return ans.max(1) as i32; 
    }
}

fn main() {
    let edges = vec![vec![0,1,10], vec![0,2,1], vec![1,2,2]];
    let max_moves = 6; 
    let n = 3; 
    assert_eq!(Solution::reachable_nodes(edges, max_moves, n), 13); 
}