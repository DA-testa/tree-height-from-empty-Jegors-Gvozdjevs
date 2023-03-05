#python3
import sys
import threading
import numpy


def compute_height(n, parents):
    list = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            ro = i
        else:
            list[parent].append(i)
    max_height = 0

    def nodes(node):
        max_depth = 0
        for child in list[node]:
            child_depth = nodes(child) + 1
            max_depth = max(max_depth, child_depth)
        return max_depth


    max_height = nodes(ro)    
    return max_height + 1


def main():
    fileorno = input()

    if "I" in fileorno or "i" in fileorno:
        n = int(input())
        parents = list(map(int, input().split()))
        ans = compute_height(n, parents)
        print(ans)

    elif "F" in fileorno or "f" in fileorno:
        file = input()
        if "a" not in file:
            with open("test/" + file, 'r')as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                ans = compute_height(n, parents)
                print(ans)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#print(numpy.array([1,2,3]))
