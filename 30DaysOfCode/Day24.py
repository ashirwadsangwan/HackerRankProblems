class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        self.head = head
        pointer1 = self.head
        
        while (pointer1!=None) and pointer1.next != None:
            pointer2 = pointer1

            while pointer2.next != None:
                if pointer2.data == pointer2.next.data:
                    dup = pointer2.next
                    pointer2.next = pointer2.next.next
                    del dup
                else:
                    pointer2 = pointer2.next

            pointer1 = pointer1.next
        return (self.head)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
