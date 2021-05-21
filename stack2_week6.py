class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        elif self.isEmpty():
            print("Stack Empty")

    def peek(self):
        if not self.isEmpty():
            print(self.top[-1])
        elif self.isEmpty():
            print("Stack Empty")

    def duplicate(self):
        if not self.isEmpty():
            ch=self.top.pop(-1)
            self.top.append(ch)
            self.top.append(ch)
            return self.top

    def printt(self):
        for i in self.top[::-1]:
            print(i,end='')

    def upRotate(self, n):
        n=int(n)
        if n<=len(self.top):
            a=self.top[-1]
            count = -1
            while count>-n:
                self.top[count] = self.top[count-1]
                count= count-1
            self.top[-n] = a
        elif n>len(self.top):
            return self.top

    def downRotate(self, n):
        n = int(n)
        if n<=len(self.top):
            b=self.top[-n]
            count=-n
            while count<-1:
                self.top[count]=self.top[count+1]
                count=count+1
            self.top[-1]=b
        elif n>len(self.top):
            return self.top



if __name__ == "__main__":
    stack=Stack()
    while True:
        instruction = input("연산의 종류(POP, PUSH, PEEK, DUP, UpR, DownR, PRINT)와 영문자를 입력하세요:")
        if instruction[0] == "P" and instruction[1]=="U" and instruction[2]=="S" and instruction[3]=="H":
            stack.push(instruction[5])
        elif instruction[0] == "P" and instruction[1] == "O" and instruction[2] == "P":
            stack.pop()
        elif instruction[0] == "P" and instruction[1]=="E" and instruction[2]=="E" and instruction[3]=="K":
            stack.peek()
        elif instruction[0] == "D" and instruction[1] == "U" and instruction[2] == "P":
            stack.duplicate()
        elif instruction[0] == "U" and instruction[1] == "p" and instruction[2] == "R":
            stack.upRotate(instruction[4])
        elif instruction[0] == "D" and instruction[1] == "o" and instruction[2] == "w" and instruction[3] == "n" and \
                instruction[4] == "R":
            stack.downRotate(instruction[6])
        elif instruction[0] == "P" and instruction[1] == "R" and instruction[2] == "I" and instruction[3] == "N" and \
                instruction[4] == "T":
            stack.printt()
            print()

