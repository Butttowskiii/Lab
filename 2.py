#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     05.10.2021
# Copyright:   (c) admin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import bisect

N, M = map(int,input().split())
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

for x in list2:
    i = bisect.bisect_left(list1, x)
    if i >= N:
        print(0)
        continue
    if list1[i] == x:
        print(i + 1, bisect.bisect(list1, x, i))
    else:
        print(0)