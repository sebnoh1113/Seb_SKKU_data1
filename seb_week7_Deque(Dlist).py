class _DoublyLinkedBase:
    class _Node:
        __slots__='_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element=element
            self._prev=prev
            self._next=next
    def __init__(self):
        self._header=self._Node(None,None,None)
        self._trailer=self._Node(None,None,None)
        self._header._next=self._trailer
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def _insert_between(self, e, predecessor, successor):
        newest= self._Node(e, predecessor, successor)
        predecessor._next=newest
        successor._prev=newest
        self._size+=1
        return newest

    def _delete_node(self, node):
        predecessor=node._prev
        successor=node._next
        predecessor._next=successor
        successor._prev=predecessor
        self._size-=1
        element=node._element
        node._prev=node._next=node._element=None
        return element

class dlinked_deque(_DoublyLinkedBase):
    def first(self):
        return self._header._next._element

    def last(self):
        return self._trailer._prev._element

    def _insert_first(self, e):
        self._insert_between(e, self._header,self._header._next)

    def _insert_last(self, e):
        self._insert_between(e,self._trailer._prev,self._trailer)

    def delete_first(self):
        return self._delete_node(self._header._next)

    def delete_last(self):
        return self._delete_node(self._trailer._prev)

    def printt(self):
        r = self._header._next
        while r != self._trailer:
            print(r._element, end=' ')
            r = r._next


if __name__ == "__main__":
    dq = dlinked_deque()
    count = 1
    n = int(input("연산의 개수:"))
    while count <= n:

        instruction = input("연산의 종류(AF, AR, DF, DR, P)와 양의 정수를 입력하세요:")
        if instruction[0] == "A" and instruction[1] =="F":
            a, b= instruction.split(" ")
            dq._insert_first(int(b))
        elif instruction[0] == "A" and instruction[1] == "R":
            a, b = instruction.split(" ")
            dq._insert_last(int(b))
        elif instruction[0] == "D" and instruction[1] == "F":
            if not dq.is_empty():
                dq.delete_first()
            if dq.is_empty():
                print("underflow")
                break
        elif instruction[0] == "D" and instruction[1] == "R":
            if not dq.is_empty():
                dq.delete_last()
            if dq.is_empty():
                print("underflow")
                break
        elif instruction[0] == "P":
            dq.printt()
            print()

        count = count + 1