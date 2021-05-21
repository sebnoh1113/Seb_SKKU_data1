class Chaining:
    class Node:
        def __init__(self, key, link):
            self.key=key
            self.next=link

    def __init__(self, size):
        self.M=size
        self.a=[None]*size

    def hash(self, key):
        return key % self.M

    def put(self, key):
        i=int(self.hash(key))
        self.a[i]=self.Node(key,self.a[i])

    def delete(self, key):
        i = self.hash(key)
        p = self.a[i]
        n = 0
        while p != None:
            n += 1
            if key == p.key:
                p.key=p.next.key
                print(n)
                break
            p = p.next
        if p == None:
            print(0)

    def get(self, key):
        i=self.hash(key)
        p=self.a[i]
        n=0
        while p!=None:
            n+=1
            if key ==p.key:
                print(n)
                break
            p=p.next
        if p==None:
            print(0)

    def print_table(self):
        for i in range(self.M):
            p = self.a[i]
            while p != None:
                print(p.key, end=' ')
                p=p.next

if __name__=="__main__":
        M=int(input("해시테이블의 사이즈:"))
        size=M
        hash=Chaining(size)
        while True:
            instruction = input("연산의 종류 등을 입력하여 주세요:")
            if instruction[0] == 'i':
                a, b = instruction.split(" ")
                hash.put(int(b))
            elif instruction[0] == "s":
                a, b = instruction.split(" ")
                hash.get(int(b))
            if instruction[0] == 'd':
                a, b = instruction.split(" ")
                hash.delete(int(b))
            elif instruction[0] == "p":
                hash.print_table()
                print()
            elif instruction[0] == "e":
                break