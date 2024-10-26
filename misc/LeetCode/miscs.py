class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)
        dummy = ListNode(0, head)
        prev, current = dummy, head
        
        while current:
            if current.val in nums:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next


s = Solution()
teste = s.modifiedList(
    [5], ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, None)))))
)
while teste:
    print(str(teste.val) + " -> ", end="")
    teste = teste.next
