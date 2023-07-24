use std::collections::VecDeque; 

// 可以把整个区间想象成一个个独立的U型区间，每次
// 只需要考虑当前的U型区间，当前的U型区间
// 会变成下一次的区间的底部

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len(); 
        let mut deque: VecDeque<(i32, i32)> = VecDeque::new(); 
        let mut water = 0; 

        for i in 0..n {      
            // initial value doesn't matter since it will never be used 
            let mut previous_bar = 0; 

            while deque.len() > 0 {
                let bar = deque.back().unwrap().0; 
                let pos = deque.back().unwrap().1; 

                // calculate water trapped by bar, previous_bar, height[i]
                if i as i32 - 1 != pos {
                    water += (bar.min(height[i]) - previous_bar) * ((i as i32 - pos - 1)); 
                }
                previous_bar = bar; 

                // if bar in stack is higher than current height, exit 
                if bar >= height[i] {
                    break; 
                } else {
                    deque.pop_back(); 
                }
            }   

            // add current to stack 
            deque.push_back((height[i], i as i32));              
        }     

        return water;      
    }
}

