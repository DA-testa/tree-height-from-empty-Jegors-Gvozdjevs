#python3
import sys
import threading
import numpy


def compute_height(n, parents):
    list = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            r = i
        else:
            list[parent].append(i)
    max_height = 0

    def nodes(node):
        max_depth = 0
        for child in list[node]:
            child_depth = nodes(child) + 1
            max_depth = max(max_depth, child_depth)
        return max_depth

    max_height = nodes(r)    
    return max_height + 1


def main():
    fileorno = input("i or f")
    ok = True
    while ok:

        if fileorno == "I":
            n = int(input("nodes"))
            parents = list(map(int, input().split()))
            ans = compute_height(n, parents)
            print(ans)
            ok = False

        if fileorno == "F":
            file =input()
            with open("test/" + file, 'r')as f:
                    n = int(file.readline())
                    parents = list(map(int, input().split()))
                    ans = compute_height(n, parents)
                    print(ans)
                    ok = False
                    

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
