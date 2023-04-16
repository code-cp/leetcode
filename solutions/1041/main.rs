// https://leetcode.cn/problems/robot-bounded-in-circle/solutions/2219798/python3javacgotypescript-yi-ti-yi-jie-mo-cyda/

impl Solution {
    pub fn is_robot_bounded(instructions: String) -> bool {
        // dist in north, west, south, east  
        let mut dist = vec![0; 4]; 
        // direction facing north, west, south, east 
        let mut dir = 0; 
        for i in instructions.as_bytes().iter() {
            let i = *i as char; 
            match i {
                // %4 since dir+1 may >4
                'L' => dir = (dir+1)%4,
                'R' => dir = (dir+3)%4,
                'G' => dist[dir] += 1, 
                _ => {}, 
            };
        }
        return (dist[0] == dist[2] && dist[1] == dist[3]) || dir != 0; 
    }
}