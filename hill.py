from board import Board
from math import comb
import time
import sys


def findQueen(b : Board, n : int):
    if(n > b.n_queen):
        return
    for i in range(len(b.map)):
        if(b.map[n][i] == 1):
            return i
    

def displayBoard(b : Board):
    for i in range(len(b.map)):
        for j in range(len(b.map)):
            if(b.map[i][j] == 0):
                b.map[i][j] = '-'
            print(b.map[i][j], end=" ")
        print()
    return b


def localSearch(b : Board, n : int, winCond = 0):
    while(b.get_fitness() != winCond):
        if(n >= len(b.map)):
            b = Board(n)
            n = 0
        c = comb(len(b.map), 2)
        while(n < len(b.map)):
            bestSpot = 0
            val = findQueen(b, n)
            b.map[n][val] = 0
            for i in range(len(b.map[n])):
                b.map[n][i] = 1
                if(b.get_fitness() < c):
                    c = b.get_fitness()
                    bestSpot = i
                b.map[n][i] = 0
            b.map[n][bestSpot] = 1
            n+=1
    return b


if __name__ == '__main__':
    # k = int(sys.argv[1])
    k = 5
    b = Board(k)
    start_time = time.time()
    if(k == 2 or k == 3):
        b_goal = localSearch(b, 0, 1)
    else:
        b_goal = localSearch(b, 0)
    endTime = ((time.time() - start_time))*1000
    print(f"Running time: {int(endTime)}ms")
    displayBoard(b_goal)