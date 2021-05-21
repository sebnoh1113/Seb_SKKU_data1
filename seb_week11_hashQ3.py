class DoubleHashing:
    def __init__(self, size):
        self.M=size
        self.a=[None]*size
        for i in range(self.M):
            if self.a[i]==None:
                self.a[i]=0
        self.N=0

    def hash(self, key):
            return key % self.M

    def put(self, key, q):
        initial_position = self.hash(key)
        i=initial_position
        d = q-(key%q)
        j=0
        while True:
            if self.a[i] == 0:
                self.a[i] = key
                self.N+=1
                print(i)
                break
            j+=1
            print('C', end='')
            i=(initial_position + j*d)%self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        d = q-(key%q)
        j = 0
        while self.a[i] !=0:
            if self.a[i]==key:
                print(i, self.a[i])
                break
            j +=1
            i=(initial_position+j*d) % self.M
        if self.a[i] == 0:
            print('-1')

    def print_hashtable(self):
        for i in range(self.M):
            print(self.a[i], end=' ')

if __name__=="__main__":
        M , q=int(input("해시테이블의 사이즈:")), int(input("해시테이블 사이즈보다 조금 작은 소수:"))
        size=M
        hash=DoubleHashing(size)
        while True:
            instruction = input("연산의 종류 등을 입력하여 주세요:")
            if instruction[0] == 'i':
                a, b = instruction.split(" ")
                hash.put(int(b), q)
            elif instruction[0] == "s":
                a, b = instruction.split(" ")
                hash.get(int(b))
            elif instruction[0] == "p":
                hash.print_hashtable()
                print()
            elif instruction[0] == "e":
                hash.print_hashtable()
                break

