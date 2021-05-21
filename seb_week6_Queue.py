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

    def dequeue(self):
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

if __name__ == "__main__":
    q=int(input("원형 큐의 크기(양의정수):"))
    MAX_QSIZE = q
    queue = CircularQueue()
    n=int(input("연산의 개수(양의정수):"))
    count=1
    while count<=n:
        instruction = input("연산의 종류 등을 입력하세요:")
        if instruction[0] == "I":
            if not queue.isFull():
                a, b, = instruction.split(" ")
                queue.enqueue(b)
            if queue.isFull():
                print("overflow", end=' ')
                queue.display()
                break
        if instruction[0] == "D":
            if not queue.isEmpty():
                queue.dequeue()
            if queue.isEmpty():
                print("underflow")
                break
        if instruction[0] == "P":
            queue.display()
            print()
        count=count+1
