# # 문제1
#
# def die1(x):
#     print(die2)
#
# def die2(x,y):
#     print(die3)
#
# def die3(x,y,z):
#     if x+y+z==N
#         return (x,y,z)
#
# N=input("3~18 사이의 숫자를 입력해 주세요:")
# int(N)
# for x in range(1,2,3,4,5,6):
#     print(die1(x))

# 문제2
#
# N = int(input("양의 정수 N을 입력하세요:"))
# M = int(input("양의 정수 M을 입력하세요:"))
#
# if N>M:
#     print("몫:",N//M)
#     print("나머지:", N%M)
# else:
#     print("몫:", M // N)
#     print("나머지:", M % N)

#문제3
# N = int(input("정수 N을 입력하세요:"))
# print(int(20<=N and N<=30))

#문제4
# N = int(input("10 이상의 양의 정수 N을 입력하세요:"))
# while(1):
#     j=list(str(N))
#     N=0
#     for i in j:
#         N+=int(i)
#     if N <10: break
# print(N)
#
# # k = int(input())
#
#
#
#
# while(1):
#
#   j = list(str(k));
#
#   k = 0;
#
#   for i in j:
#
#     k += int(i);
#
#   if k < 10: break;
#
#
#
#
# print (k)

def seb1(A): # 함수 헤더 seb은 함수 이름, A는 매개변수목록
	sum = A+1   # 이하 함수 몸통
	return sum