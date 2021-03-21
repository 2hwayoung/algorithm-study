# https://www.acmicpc.net/problem/6581

# 80글자 이하
# '<'나 '>' 포함하지 않는다
# <br>와 <hr>만 존재

import sys

curlen = 0
# sys.stdin = open("input.txt","r")

while (True) :
    try:
        for word in input().split():
            if word == '<br>':
                curlen = 0
                print()
            elif word == '<hr>':
                if curlen != 0:
                    print('\n'+'-'*80)
                else:
                    print('-'*80)
                curlen = 0
            else:
                if curlen + len(word) + 1 <= 80:
                    if curlen:
                        print(' '+word, end='')
                        curlen += len(word) + 1
                    else:
                        print(word, end='')
                        curlen = len(word)
                else:
                    print('\n'+word, end='')
                    curlen = len(word)
    except:
        break