class bottom_up_Heap():
    def __init__ (self):
        self.heap=[]
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size()==0
    def Left(self, i): return int(self.heap[i*2])
    def Right(self, i): return int(self.heap[i*2+1])


    def heap2(self, n):
        self.heap=self.heap+n
        i=self.size()
        p= i//2
        if i % 2 == 0:
            parent = int(self.heap[p])
            if parent < self.Left(p):
                self.heap[p] = self.Left(p)
                self.heap[p * 2] = parent
            p=p-1
            while p >= 1:
                parent = int(self.heap[p])
                if parent < self.Left(p) and parent < self.Right(p):
                    if self.Left(p) < self.Right(p):
                        self.heap[p] = self.Right(p)
                        self.heap[p * 2 + 1] = parent
                    elif self.Right(p) < self.Left(p):
                        self.heap[p] = self.Left(p)
                        self.heap[p * 2] = parent
                elif parent < self.Left(p):
                    self.heap[p] = self.Left(p)
                    self.heap[p * 2] = parent
                elif parent < self.Right(p):
                    self.heap[p] = self.Right(p)
                    self.heap[p * 2 + 1] = parent
                p = p - 1
        elif i%2!=0:
            while p>=1:
                parent= int(self.heap[p])
                if parent<self.Left(p) and parent<self.Right(p):
                    if self.Left(p)< self.Right(p):
                        self.heap[p]=self.Right(p)
                        self.heap[p * 2 + 1] = parent
                    elif self.Right(p)< self.Left(p):
                        self.heap[p] = self.Left(p)
                        self.heap[p * 2] = parent
                elif parent < self.Left(p):
                    self.heap[p] = self.Left(p)
                    self.heap[p * 2] = parent
                elif parent<self.Right(p):
                    self.heap[p] = self.Right(p)
                    self.heap[p * 2 + 1] = parent
                p=p-1

        print('  ', end='')
        for i in self.heap[1:]:
            print(i, end=' ')


if __name__ == "__main__":

    heap=bottom_up_Heap()
    key_num=input('키 개수(100개 미만):')
    key_contents=input('키 내용(중복이 없는 1이상의 정수):')
    data = key_contents.split(' ')
    heap.heap2(data)
