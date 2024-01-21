impl Solution {
    pub fn day_of_year(date: String) -> i32 {
        let is_leap_year = |year: i32| -> bool {
            if year % 400 == 0 || (year % 4 == 0 && year % 100 != 0) {
                true 
            } else {
                false 
            }
        }; 

        let date = date.split("-").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>(); 
        let (year, month, day) = (date[0], date[1], date[2]);  

        let mut month_days = vec![31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30];
        if is_leap_year(year) {
            month_days[1] += 1; 
        }

        let ans = &month_days[..month as usize - 1].iter().sum() + day;

        ans  
    }
}