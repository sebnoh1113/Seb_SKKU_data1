class Dlist:
    class Node:
        def __init__(self, e, prev, link):
            self.e = e
            self.prev = prev
            self.link = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.link = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, r, e):
        if r == self.head:
            print("invalid position.")
        else:
            t = r.prev
            print(t)
            n = self.Node(e, t, r)
            r.prev = n
            t.link = n
            self.size += 1

    def delete(self, r):
        if r == self.head:
            print("invalid position.")
        else:
            a = r.prev
            b = r.link
            a.link = b
            b.prev = a
            self.size -= 1

    def get_order(self, n):
        self.cursor = self.head
        if self.size + 1 >= n > 0:
            for i in range(n):
                self.cursor = self.cursor.link
        else:
            print("invalid position.")
        return self.cursor

    def pprintt(self):
        r = self.head.link
        while r != self.tail:
            print(r.e, end='')
            r = r.link


d_list = Dlist()

count = 1
n = int(input("연산의 개수:"))
while count <= n:

    instruction = input("")
    if instruction[0] == "A":
        a, b, c = instruction.split(" ")
        d_list.add(d_list.get_order(int(b)), c)
    elif instruction[0] == "D":
        a, b = instruction.split(" ")
        d_list.delete(d_list.get_order(int(b)))
    elif instruction[0] == "G":
        a, b = instruction.split(" ")
        print(d_list.get_order(int(b)).e)
    elif instruction[0] == "P":
        a = "P"
        d_list.pprintt()

    count = count + 1
