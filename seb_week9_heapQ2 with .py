# # min/max
# # down/up
# # 삽입식(upheap 방식을 사용)
# # 비삽입식
# #    bottom-up : downheap 작동을 bottom up 방향으로 반복 수행
# #    topdown 더 좋은가?
# 1. 코딩스타일 (클래스 대문자 / 설명적 변수명 / implicit error avoidance / 풍부한 주석) 2. 검증 코드

import random
import math
import sys

#
# class Bottom_up_Heap():
#     def __init__ (self, heap):
#         self.heap=heap
#
#     def Left(self, i): return int(self.heap[i*2])
#     def Right(self, i): return int(self.heap[i*2+1])
#     def heap2(self,n):
#
#         i=int(n)
#         p = i // 2
#
#         while p >= 1:
#             print()
#             print()
#             print('--------------p', p)
#             print()
#             child = p * 2
#             p_node = p
#
#             while child <= i:
#
#                 if child < i and self.Left(p_node) < self.Right(p_node): # out of range risk
#                     child += 1
#                     print('child+', child)
#
#                 print('p node value ', self.heap[p_node])
#                 print('child node value ', self.heap[child])
#                 if int(self.heap[p_node]) < int(self.heap[child]):
#                     tmp = self.heap[p_node]
#                     self.heap[p_node] = self.heap[child]
#                     self.heap[child] = tmp
#                     print('p to be changed', p_node)
#                     print('child to be changed', child)
#                     print('changed p node value ', self.heap[p_node])
#                     print('changed child value ', self.heap[child])
#
#                 p_node = child
#                 child = child*2
#
#             p = p - 1
#
#             print('  ', end='')
#             kk = self.heap[1:]
#             for ii in kk:
#                 print(ii, end=' ')
#
#         return self.heap

class Bottom_up_Heap():

    def __init__(self, heap):
        self.heap = heap

    def Left(self, i):
        return int(self.heap[i * 2])

    def Right(self, i):
        return int(self.heap[i * 2 + 1])

    def heap2(self, n):

        i = int(n)
        p = i // 2
        while p >= 1:
            parent = p
            child = p * 2
            p_node = int(self.heap[p])
            while child <= i:
                if child < i and self.Left(parent) < self.Right(parent):
                    child += 1
                if p_node >= int(self.heap[child]):
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = p_node
            p = p - 1
        print('  ', end='')
        for i in self.heap[1:]:
            print(i, end=' ')
        return self.heap


if __name__ == "__main__":

    num_key = random.randint(1, 100)
    heapList = [0]
    for i in range(num_key):
        heapList.append(random.randint(0, 1000))
    print(heapList)
    print()
    print("Start!")
    print()

    heap = Bottom_up_Heap(heapList)
    maxHeap = heap.heap2(num_key)
    print()

    # 부모 노드가 있는 층의 개수 계산
    left_parent_number = int(math.log2(num_key))
    print()
    print('layer no: ', left_parent_number + 1)

    # 부모 노드의 개수
    parent_number = int(num_key / 2)
    print('parent number: ', parent_number)
    if parent_number == 0:
        print()
        print("Done")
        sys.exit()

    # 마지막 부모 노드가 오른쪽 자식 노드를 갖는지 여부
    if (num_key / 2) % 1 == 0:
        lastRightChild = False
    else:
        lastRightChild = True

    # maxHeap 여부 검증
    for i in range(left_parent_number):
        print()
        print('%d layer: ' % (i + 1))

        for k in range(2 ** i):
            p_index = (2 ** i) + k
            print()
            print('+++++ %d parent node: ' % p_index)

            if p_index == parent_number:
                if lastRightChild:

                    if maxHeap[p_index] >= maxHeap[p_index * 2] and maxHeap[p_index] >= maxHeap[p_index * 2 + 1]:
                        print()
                        print("Good")
                    else:
                        print()
                        print("Not verified")
                        print(maxHeap[p_index])
                        print(maxHeap[p_index * 2])
                        print(maxHeap[p_index * 2 + 1])
                        sys.exit()
                else:

                    if maxHeap[p_index] >= maxHeap[p_index * 2]:
                        print()
                        print("Good")
                    else:
                        print()
                        print("Not verified")
                        print(maxHeap[p_index])
                        print(maxHeap[p_index * 2])
                        sys.exit()
            else:
                if maxHeap[p_index] >= maxHeap[p_index * 2] and maxHeap[p_index] >= maxHeap[p_index * 2 + 1]:
                    print()
                    print("Good")
                else:
                    print()
                    print("Not verified")
                    print('p_index ', p_index)
                    print(maxHeap[p_index])
                    print(maxHeap[p_index * 2])
                    print(maxHeap[p_index * 2 + 1])
                    sys.exit()

            if p_index >= parent_number :
                print()
                print("Done")
                sys.exit()

# class Bottom_up_Heap():
#     def __init__ (self, heap):
#         self.heap=heap
#
#     def Left(self, i): return int(self.heap[i*2])
#     def Right(self, i): return int(self.heap[i*2+1])
#     def heap2(self,n):
#
#         i=int(n)
#         p = i // 2
#
#         while p >= 1:
#             print()
#             print()
#             print('--------------p', p)
#             print()
#             child = p * 2
#             p_node = p
#
#             while child <= i:
#
#                 if child < i and self.Left(p_node) < self.Right(p_node): # out of range risk
#                     child += 1
#                     print('child+', child)
#
#                 print('p node value ', self.heap[p_node])
#                 print('child node value ', self.heap[child])
#                 if int(self.heap[p_node]) < int(self.heap[child]):
#                     tmp = self.heap[p_node]
#                     self.heap[p_node] = self.heap[child]
#                     self.heap[child] = tmp
#                     print('p to be changed', p_node)
#                     print('child to be changed', child)
#                     print('changed p node value ', self.heap[p_node])
#                     print('changed child value ', self.heap[child])
#
#                 p_node = child
#                 child = child*2
#
#             p = p - 1
#
#             print('  ', end='')
#             kk = self.heap[1:]
#             for ii in kk:
#                 print(ii, end=' ')
#
# if __name__ == "__main__":
#     heap = Bottom_up_Heap()
#     num_key, key_contents = input('키 개수(100개 미만):'), input('키 내용(중복이 없는 1이상의 정수):')
#     data = key_contents.split(' ')
#     heap.heap2(data,num_key)

# #
# class bottom_up_Heap():
#     def __init__ (self):
#         self.heap=[]
#         self.heap.append(0)
#
#     def Left(self, i): return int(self.heap[i*2])
#     def Right(self, i): return int(self.heap[i*2+1])
#     def heap2(self,k,n):
#         self.heap=self.heap+k
#         i=int(n)
#         p = i // 2
#         while p >= 1:
#             parent = p
#             child = p * 2
#             p_node = int(self.heap[p])
#             while child <= i:
#                 if child < i and self.Left(parent) < self.Right(parent):
#                     child += 1
#                 if p_node >= int(self.heap[child]):
#                     break
#                 self.heap[parent] = self.heap[child]
#                 parent = child
#                 child *=2
#             self.heap[parent] = p_node
#             p=p-1
#         print('  ', end='')
#         for i in self.heap[1:]:
#             print(i, end=' ')
#
# if __name__ == "__main__":
#     heap = bottom_up_Heap()
#     num_key, key_contents = input('키 개수(100개 미만):'), input('키 내용(중복이 없는 1이상의 정수):')
#     data = key_contents.split(' ')
#     heap.heap2(data,num_key)