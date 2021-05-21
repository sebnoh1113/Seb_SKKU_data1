class LinearProbing:
    def __init__(self, size):
        self.M=size
        self.a=[None]*size
        for i in range(self.M):
            if self.a[i]==None:
                self.a[i]=0

    def hash(self, key):
            return key % self.M

    def put(self, key):
        initial_position = self.hash(key)
        i=initial_position
        j=0
        while True:
            if self.a[i] == 0:
                self.a[i] = key
                print(i)
                break
            j+=1
            i=(initial_position+j)%self.M
            print('C', end='')
            if i == initial_position:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j=0
        while self.a[i] !=0:
            if self.a[i]==key:
                print(i, self.a[i])
                break
            i=(initial_position+j) % self. M
            j +=1
            if i == initial_position:
                print('-1')
        if self.a[i]==0:
            print('-1')

if __name__=="__main__":
        M=int(input("해시테이블의 사이즈:"))
        size=M
        hash=LinearProbing(size)
        while True:
            instruction = input("연산의 종류 등을 입력하여 주세요:")
            if instruction[0] == 'i':
                a, b = instruction.split(" ")
                hash.put(int(b))
            elif instruction[0] == "s":
                a, b = instruction.split(" ")
                hash.get(int(b))
            elif instruction[0] == "e":
                break



