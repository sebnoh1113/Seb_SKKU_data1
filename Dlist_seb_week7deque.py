class DNode:
    def __init__(self, item, prev=None, next=None):
        self.data = item
        self.prev = prev
        self.next = next


class dlinked_deque():

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def addFront(self, item):
        if (self.isEmpty()):
            node = DNode(item, None, None)
            self.front = node
            self.rear = node
        else:
            node = DNode(item, None, self.front)
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        if (self.isEmpty()):
            node = DNode(item, None, None)
            self.front = node
            self.rear = node
        else:
            node = DNode(item, self.rear, None)
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

    def printt(self):
        flag = True
        p = self.front
        while p:
            if p != self.rear:

                if flag == True:
                    print('  ' + str(p.data), end=' ')
                    flag = flag and False
                else:
                    print(str(p.data), end=' ')

                p = p.next
            else:

                if flag == True:
                    print('  ' + str(p.data))
                    flag = flag and False
                else:
                    print(str(p.data))

                break


if __name__ == "__main__":
    dq = dlinked_deque()
    count = 1
    n = int(input("연산의 개수:"))
    while count <= n:

        instruction = input("연산의 종류(AF, AR, DF, DR, P)와 양의 정수를 입력하세요:")
        if instruction[0] == "A" and instruction[1] == "F":
            a, b = instruction.split(" ")
            dq.addFront(int(b))
        elif instruction[0] == "A" and instruction[1] == "R":
            a, b = instruction.split(" ")
            dq.addRear(int(b))
        elif instruction[0] == "D" and instruction[1] == "F":
            if dq.isEmpty():
                print("underflow")
                break
            if not dq.isEmpty():
                dq.deleteFront()

        elif instruction[0] == "D" and instruction[1] == "R":
            if dq.isEmpty():
                print("underflow")
                break
            if not dq.isEmpty():
                dq.deleteRear()

        elif instruction[0] == "P":
            dq.printt()

        count = count + 1