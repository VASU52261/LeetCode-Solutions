
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null||head.next==null)
        return head;
        ListNode prev=null;
        ListNode cur=head;
        while(head!=null)
        {
            head=head.next;
            cur.next=prev;
            prev=cur;
            cur=head;
        }
        return prev;
    }
}
