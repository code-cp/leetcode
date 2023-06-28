impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        let circle_x1 = x_center - radius;
        let circle_y1 = y_center - radius;
        let circle_x2 = x_center + radius;
        let circle_y2 = y_center + radius;

        for i in circle_x1..=circle_x2 {
            for j in circle_y1..=circle_y2 {
                if (i-x_center).pow(2) + (j-y_center).pow(2) > radius.pow(2) {
                    continue; 
                }
                if i < x1 || i > x2 {
                    continue; 
                }
                if j < y1 || j > y2 {
                    continue; 
                }
                return true; 
            }
        }

        return false; 
    }
}