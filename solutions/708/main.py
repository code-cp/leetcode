# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/4ueAj6
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # if input is empty 
        if head is None: 
            head = Node(insertVal)
            head.next = head 
            return head 
        res = head 
        insert = Node(insertVal)
        # if insert is larger than max or smaller than min 
        min_node = head 
        max_node = head 
        while head: 
            head = head.next
            if res == head: 
                break 
            if head.val <= min_node.val: 
                min_node = head 
            if head.val >= max_node.val: 
                max_node = head 
        if min_node.val >= insertVal or max_node.val <= insertVal: 
            temp = max_node.next 
            head = max_node
            head.next = insert  
            insert.next = temp
            return res 
        # if insert is within [min, max]
        head = min_node 
        while head: 
            if head.val > insertVal: 
                break 
            pre_node = head
            head = head.next 
        pre_node.next = insert  
        insert.next = head
        return res  