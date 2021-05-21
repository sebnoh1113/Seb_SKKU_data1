MAX_QSIZE=10
class CircularQueue:

    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[0]*MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear=(self.rear+1)%MAX_QSIZE
            self.items[self.rear]=item

    def dequeue(self): #후단 삭제
        if not self.isEmpty():
            self.front=(self.front+1)%MAX_QSIZE
            self.items[self.front]=0

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]

    def size(self):
        return(self.rear- self.front+MAX_QSIZE)%MAX_QSIZE

    def display(self):
        for i in self.items[:]:
            print(i,end=' ')

class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front]=item
            self.front=self.front-1
            if self.front<0:self.front=MAX_QSIZE-1

    def deleteRear(self):
        if not self.isEmpty():
            item=self.items[self.rear]
            self.rear=self.rear-1
            if self.rear<0:self.rear=MAX_QSIZE-1
            return item

    def getRear(self):
        return self.items[self.rear]



if __name__ == "__main__":
    dq = CircularDeque()
    count = 1
    n = int(input("연산의 개수:"))
    while count <= n:

        instruction = input("연산의 종류(AF, AR, DF, DR, P)와 양의 정수를 입력하세요:")
        if instruction[0] == "A" and instruction[1] == "F":
            a, b = instruction.split(" ")
            dq.addFront(int(b))
        elif instruction[0] == "A" and instruction[1] == "F":
            a, b = instruction.split(" ")
            dq.addRear(int(b))
        elif instruction[0] == "D" and instruction[1] == "F":
            if not dq.isEmpty():
                dq.deleteFront()
            if dq.isEmpty():
                print("underflow")
                break
        elif instruction[0] == "D" and instruction[1] == "R":
            if not dq.isEmpty():
                dq.deleteRear()
            if dq.isEmpty():
                print("underflow")
                break
        elif instruction[0] == "P":
            dq.display()
            print()

        count = count + 1