pub struct NumArray {
    buf: Vec<i32>, 
    n: i32, 
}

impl NumArray {
    pub fn new(nums: Vec<i32>) -> Self {
        let n: usize = nums.len(); 
        let mut buf = vec![0 as i32; 2*n]; 
        buf[n..2*n].copy_from_slice(&nums); 
        for i in (1..n).rev() {
            buf[i] = buf[2*i] + buf[2*i+1]; 
        }
        NumArray {buf: buf, n: n as i32} 
    }

    fn update(&mut self, index: i32, val: i32) {
        let mut idx = index + self.n;
        self.buf[idx as usize] = val; 
        idx /= 2; 

        while idx != 0 {
            self.buf[idx as usize] = self.buf[2*idx as usize] + self.buf[(2*idx+1) as usize]; 
            idx /= 2; 
        }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let mut l = left + self.n;
        let mut r = right + self.n;
        let mut ans = 0;
        while l <= r {
            if l % 2 == 1 {
                ans += self.buf[l as usize]; 
                l += 1; 
            }
            if r % 2 == 0 {
                ans += self.buf[r as usize];
                r -= 1;
            }
            l /= 2;
            r /= 2;
        }
        return ans;  
    }
}

fn main() {
    let nums = vec![1, 3, 5]; 
    let mut obj = NumArray::new(nums);
    let ret_1: i32 = obj.sum_range(0, 2);
    assert_eq!(ret_1, 9);
    obj.update(1, 2);
    let ret_2: i32 = obj.sum_range(0, 2);
    assert_eq!(ret_2, 8);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let nums = vec![9, -8]; 
        let mut obj = NumArray::new(nums);
        obj.update(0, 3);
        let ret_1: i32 = obj.sum_range(1, 1);
        assert_eq!(ret_1, -8);
        let ret_2: i32 = obj.sum_range(0, 1);
        assert_eq!(ret_2, -5);
        obj.update(1, -3);
        let ret_3: i32 = obj.sum_range(0, 1);
        assert_eq!(ret_3, 0);
    }

    #[test]
    fn test2() {
        let nums = vec![0,9,5,7,3]; 
        let mut obj = NumArray::new(nums);
        let ret_1: i32 = obj.sum_range(4, 4);
        assert_eq!(ret_1, 3);
    }
}
