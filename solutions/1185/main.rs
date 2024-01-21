impl Solution {
    pub fn day_of_the_week(day: i32, month: i32, year: i32) -> String {
        let is_leap_year = | year: i32 | -> bool {
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
                true
            } else {
                false
            }
        };

        let start_year = 1971; 
        let mut days = (start_year..year)
            .into_iter()
            .fold(0, |acc, y| acc + 365 + if is_leap_year(y) {1} else {0}); 

        let mut month_days = vec![31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30];
        if is_leap_year(year) {
            month_days[1] += 1; 
        }
        // NOTE, cannot use month_days, need to use &month_days 
        days += &month_days[..month as usize - 1].iter().sum(); 
        let is_leap_year = | year: i32 | -> bool {
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
                true
            } else {
                false
            }
        };
        
        days += day; 
        let week = vec!["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        // 1970 年 12 月 31 日是星期四
        week[(days as usize + 3) % 7].to_owned()
    }
}