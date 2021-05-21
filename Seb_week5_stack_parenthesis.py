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

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def checkBrackets(statement):

    stack=Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch=='}' and left !='{') or\
                   (ch==']' and left !='[') or\
                   (ch==')' and left !='('):
                    return False

    return stack.isEmpty()

if __name__ == "__main__":
    sentence=str(str(input("1000개 이하의 문자로 구성된 수식문장을 입력하세요:")))
    a = sentence.count('{')
    b = sentence.count('[')
    c = sentence.count('(')
    d = sentence.count('}')
    e = sentence.count(']')
    f = sentence.count(')')
    N = a+b+c+d+e+f
    if len(sentence)<=1000:
        result=checkBrackets(sentence)
        if result == False:
            print('Wrong_%d' %N)
        elif result == True:
            print('Ok_%d' %N)
    else:
        print("수식문장이 1000개의 문자를 넘었습니다.")