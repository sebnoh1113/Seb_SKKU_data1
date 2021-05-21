import Seb_week5_stack_parenthesis as sw
sentence=str(str(input("1000개 이하의 문자로 구성된 수식문장을 입력하세요:")))
a = sentence.count('{')
b = sentence.count('[')
c = sentence.count('(')
d = sentence.count('}')
e = sentence.count(']')
f = sentence.count(')')
N = a+b+c+d+e+f
stack = sw.Stack()
if len(sentence)<=1000:
    result=sw.checkBrackets(sentence, stack)
    if result == False:
        print('Wrong_%d' %N)
    elif result == True:
        print('Ok_%d' %N)
else:
    print("수식문장이 1000개의 문자를 넘었습니다.")