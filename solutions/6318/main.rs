struct Solution;

impl Solution {
    fn find_minimum_time(tasks: Vec<Vec<i32>>) -> i32 {
        let mut time_dur = Vec::new();
        // step 1 
        for (i, task) in tasks.iter().enumerate() {
            let (start, end, dur) = (task[0], task[1], task[2]);
            time_dur.push((start, 0, dur, i));
            time_dur.push((end, 1, dur, i));
        }

        time_dur.sort();
        let mut active_tasks = std::collections::HashMap::new();
        let mut res = 0;
        for task in time_dur {
            let (t, state, dur, idx) = task;
            if state == 0 {
                // this is start of task
                active_tasks.insert(idx as usize,[t,dur]);
            } else {
                // this is end of task
                if let Some(val) = active_tasks.get(&idx) 
                {
                    let dur = val[1]; 
                    res += dur; 
                    let mut completed_tasks = Vec::new();
                    // step 2 
                    for (k, v) in active_tasks.iter_mut() {
                        let delta = std::cmp::min(v[1], t - v[0] + 1);
                        // NOTE, up to time t, only turned on for dur time 
                        let delta = std::cmp::min(delta, dur); 
                        *v.get_mut(1).unwrap() -= delta;
                        *v.get_mut(0).unwrap() += delta;
                        if v[1] == 0 {
                            completed_tasks.push(k.clone());
                        }
                    }
                    // step 3 house keeping 
                    // NOTE, it's OK to delete since we will do step 2 for some later time 
                    for k in completed_tasks {
                        active_tasks.remove(&k);
                    }
                }
            }
        }

        return res;
    }
}