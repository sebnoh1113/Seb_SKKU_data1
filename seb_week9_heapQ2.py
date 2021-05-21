class bottom_up_Heap():
    def __init__ (self):
        self.heap=[]
        self.heap.append(0)
    def Left(self, i): return int(self.heap[i*2])
    def Right(self, i): return int(self.heap[i*2+1])
    def heap2(self,k,n):
        self.heap=self.heap+k
        i=int(n)
        p = i // 2
        while p >= 1:
            parent = p
            child = p * 2
            p_node = int(self.heap[p])
            while child <= i:
                if child < i and self.Left(parent) < self.Right(parent):
                    child += 1
                if p_node < int(self.heap[child]):
                    self.heap[parent] = self.heap[child]
                    parent = child
                    child *= 2
            self.heap[parent] = p_node
            p=p-1
        print('  ', end='')
        for i in self.heap[1:]:
            print(i, end=' ')

if __name__ == "__main__":
    heap = bottom_up_Heap()
    num_key, key_contents = input('키 개수(100개 미만):'), input('키 내용(중복이 없는 1이상의 정수):')
    data = key_contents.split(' ')
    heap.heap2(data,num_key)