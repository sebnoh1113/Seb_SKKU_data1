class MaxHeap():
    def __init__ (self):
        self.heap=[]
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size()==0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2+1]

    def insert(self, n):
        self.heap.append(n)
        i=self.size()
        while (i !=1 and n>self.Parent(i)):
            self.heap[i]=self.Parent(i)
            i=i//2
        self.heap[i]=n
        print(0)

    def delete(self):
        parent=1
        child=2
        if not self.isEmpty():
            hroot=self.heap[1]
            last=self.heap[self.size()]
            while (child <= self.size()):
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child +=1
                if last >= self.heap[child]:
                    break
                self.heap[parent]=self.heap[child]
                parent=child
                child *=2

            self.heap[parent]=last
            self.heap.pop(-1)
            return hroot

    def display(self):
        print('  ', end='')
        for i in self.heap[1:]:
            print(i, end=' ')


if __name__ == "__main__":

    heap=MaxHeap()
    while True and heap.size()<100:
        instruction = input("연산의 종류(i와 1 이상의 정수, d, p, q)를 입력하세요:")
        if instruction[0] == 'i':
            a, b = instruction.split(" ")
            heap.insert(int(b))
        elif instruction[0] == "d":
            print(heap.delete())
        elif instruction[0] == "p":
            heap.display()
            print()
        elif instruction[0] == "q":
            break

