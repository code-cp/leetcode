use rand::Rng;

impl Solution {
    pub fn partition<T: PartialOrd>(nums: &mut Vec<T>, left: usize, right: usize) -> usize {
        let t: usize = rand::thread_rng().gen_range(left..right+1);
        nums.swap(right, t); 

        let mut i: usize = left; 
        for j in left..right {
            if nums[j] <= nums[right] {
                nums.swap(i, j); 
                i += 1;
            } 
        }
        nums.swap(i, right); 
        i 
    }
    pub fn qselect<T: PartialOrd>(nums: &mut Vec<T>, left: usize, right: usize, k: usize) -> &T {
        if left != right {
            let pivot = Solution::partition(nums, left, right); 
            if k == pivot {
                &nums[k] 
            } else if k < pivot {
                Solution::qselect(nums, left, pivot - 1, k)
            } else {
                Solution::qselect(nums, pivot + 1, right, k)
            }
        } else {
            &nums[left]
        }
    }
    pub fn min_moves2(nums: &mut Vec<i32>) -> i32 {
        let k: usize = nums.len() as usize / 2; 
        let len: usize = nums.len(); 
        let m: i32 = *Solution::qselect(nums, 0, len - 1, k); 
        nums.iter().fold(0, |acc, x| acc + (x - m).abs())
    }
}

struct Solution {}

fn main() {
    assert_eq!(2, Solution::min_moves2(&mut vec![1,2,3]));
}