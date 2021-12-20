#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     06.10.2021
# Copyright:   (c) admin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from collections import deque
n = int(input())
q = deque()
qt = deque()
res = []
k1 = 0
k2 = 0
for i in range(n):
    t1 = input().split()
    if  "-" in t1:
        res.append(q.popleft())
        k1 -= 1
    elif  '+' in t1:
        qt.append(t1[-1])
        k2 += 1
    else :
        qt.appendleft(t1[-1])
        k2 += 1
    if k1 < k2:
        q.append(qt.popleft())
        k2 -= 1
        k1 += 1
print(*res, sep='\n')