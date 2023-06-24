// For each cell, it has 3 options, either it is empty, or contains an introvert, or an extrovert.
// You can do DP where you maintain the state of the previous row, the number of remaining introverts and extroverts, the current row and column, and try the 3 options for each cell.

impl Solution {
    pub fn get_max_grid_happiness(m: i32, n: i32, introverts_count: i32, extroverts_count: i32) -> i32 {
        let dims = vec![6,7,7,3usize.pow(5)]; 
        let mut dp: Vec<Vec<Vec<Vec<i32>>>> = vec![vec![vec![vec![i32::MIN; dims[3]]; dims[2]]; dims[1]]; dims[0]]; 

        let max_state = 3usize.pow(n as u32); 
        let mut ans = 0; 

        dp[0][0][0][0] = 0; 

        // this only depends on cur state 
        let count_people = |state: usize| -> (i32, i32) {
            let mut state = state; 
            let mut count1 = 0; 
            let mut count2 = 0; 

            while state > 0 {
                let r = state % 3; 
                if r == 1 {
                    count1 += 1; 
                } else if r == 2 {
                    count2 += 1; 
                }
                state /= 3; 
            }

            (count1, count2)
        };

        let mut people = vec![vec![0, 2]; max_state]; 
        for state in 0..max_state {
            let (c1, c2) = count_people(state); 
            people[state][0] = c1; 
            people[state][1] = c2; 
        }

        // this only depends on previous and current state, and n 
        let compute_score = |pre: usize, cur: usize| -> i32 {
            let base_3 = |num: usize| -> Vec<usize> {
                let mut n = num; 
                let digits: Vec<usize> = (0..6).map(|_| {let digit = n % 3; n /= 3; digit}).collect();
                digits 
            };            

            let p = base_3(pre); 
            let q = base_3(cur); 
            let mut res = 0;

            for i in 0..n {
                if q[i as usize] == 1 {
                    res += 120;
                    if i >= 1 && q[(i - 1) as usize] > 0 {
                        res -= 30;
                    }
                    if i + 1 < n && q[(i + 1) as usize] > 0 {
                        res -= 30;
                    }
                    if p[i as usize] > 0 {
                        res -= 30;
                    }

                    if p[i as usize] == 1 {
                        res -= 30;
                    } else if p[i as usize] == 2 {
                        res += 20;
                    }
                } else if q[i as usize] == 2 {
                    res += 40;
                    if i > 0 && q[(i - 1) as usize] > 0 {
                        res += 20;
                    }
                    if i < n - 1 && q[(i + 1) as usize] > 0 {
                        res += 20;
                    }
                    if p[i as usize] > 0 {
                        res += 20;
                    }

                    if p[i as usize] == 1 {
                        res -= 30;
                    } else if p[i as usize] == 2 {
                        res += 20;
                    }
                }
            }

            res
        }; 

        let mut scores = vec![vec![0; max_state]; max_state]; 
        for pre in 0..max_state {
            for cur in 0..max_state {
                scores[pre][cur] = compute_score(pre, cur); 
            }
        }

        for i in 1..=m {
            for x in 0..=introverts_count {
                for y in 0..=extroverts_count {
                    for state in 0..max_state {
                        let (a, b) = (people[state][0], people[state][1]); 
                        if a > x || b > y {
                            continue;
                        }
                        for pre_state in 0..max_state {
                            if !(dp[(i-1) as usize][(x-a) as usize][(y-b) as usize][pre_state] as f32).is_finite() {
                                continue; 
                            }
                            dp[i as usize][x as usize][y as usize][state] = dp[i as usize][x as usize][y as usize][state].max(
                                dp[(i-1) as usize][(x-a) as usize][(y-b) as usize][pre_state] + scores[pre_state][state]
                            )
                        }
                        if i == m {
                            ans = ans.max(dp[i as usize][x as usize][y as usize][state]); 
                        }
                    }
                }
            }
        }

        ans 
    }
}