#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      admin
#
# Created:     01.11.2021
# Copyright:   (c) admin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n = int(input())
strings = [input() for i in range(n)]
strings = [(strings[i], len(strings[i])) for i in range(n)]

strings = sorted(strings, key=lambda string: string[1])
stringg = strings[0][0]
answer = ""
for i in range(len(stringg)):
        for j in range(i, len(stringg)):
            s = stringg[i:j + 1]
            if len(s) < len(answer):
                continue
            b = True
            for string in strings[1:]:
                if s not in string[0]:
                    b = False
                    break
            if b:
                answer = s

print(answer)