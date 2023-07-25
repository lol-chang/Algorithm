# https://www.acmicpc.net/problem/1018

# [출처] : https://blog.naver.com/allop24/222894537535

import sys

N, M = map(int, sys.stdin.readline().split())
ChessA = ['WB'*4, 'BW'*4, 'WB'*4, 'BW'*4, 'WB'*4, 'BW'*4, 'WB'*4, 'BW'*4]
ChessB = ['BW'*4, 'WB'*4, 'BW'*4, 'WB'*4, 'BW'*4, 'WB'*4, 'BW'*4, 'WB'*4]

Board = []
for i in range(N):
    Board.append(sys.stdin.readline().rstrip())

diff_min = 64
for row in range(N-7):
    for col in range(M-7):
        diff_A, diff_B = 0, 0
        for i in range(8):
            for j in range(8):
                if Board[row+i][col+j] != ChessA[i][j]:
                    diff_A += 1
                if Board[row+i][col+j] != ChessB[i][j]:
                    diff_B += 1
        diff_min = min(diff_min, diff_A, diff_B)
        
        if diff_min == 0:
            break
    
print(diff_min)
