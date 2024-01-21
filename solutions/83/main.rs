// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution {}

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return head; 
        }
        let mut head = head; 
        let mut node = head.as_mut().unwrap();
        let mut cur = node.val; 
        while let Some(next) = node.next.take() {
            if next.val == cur {
                node.next = next.next; 
            } else {
                cur = next.val; 
                node.next = Some(next); 
                node = node.next.as_mut().unwrap(); 
            }
        }
        head 
    }
}

#[cfg(test)]
mod tests {
    use crate::ListNode;
    use crate::Solution; 

    fn build_list_from_slice(s: &[i32]) -> Option<Box<ListNode>> {
        if s.is_empty() {
            return None; 
        }
        let head = Box::new(
            ListNode {
                val: s.first().copied().unwrap(), 
                next: build_list_from_slice(&s[1..]), 
            }
        );
        Some(head)
    }

    #[test]
    fn test_delete_duplicates() {
        struct TestCase {
            name: &'static str, 
            nums: &'static [i32], 
            expect: &'static [i32], 
        }

        vec![
            TestCase {
                name: "basic", 
                nums: &[1,1,2,2,3,3], 
                expect: &[1,2,3], 
            },
        ].iter().for_each(
            | testcase | {
                let head = build_list_from_slice(testcase.nums);
                let actual = Solution::delete_duplicates(head); 
                let expect = build_list_from_slice(testcase.expect);
                assert_eq!(expect, actual, "{} failed", testcase.name); 
            }
        ); 
    }
}