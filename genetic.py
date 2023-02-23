import sys
import time
from board import Board
import random
import numpy as np
from math import comb
"""
POTENTIAL TIME SAVE: when Natural Selection occurs, we come out with a successor. Hear me out...
With that successor, what if we took them and mutated their genes to potentially breed a better
version if not a potential solution........
"""


def findQueen(b : Board, n : int):
    if(n >= len(b.map)):
        return
    for i in range(len(b.map)):
        if(b.map[n][i] == 1):
            return i+1


def nullBoard(b : Board):
    for i in range(len(b.map)):
        one = findQueen(b, i)   
        b.map[i][one-1] = 0
    return b      


def conflictTotal(arr):
    conflictTotal = 0
    for i in range(len(arr)):
        conflictTotal += arr[i][1]
    return conflictTotal

def initialization(b : Board, elite : bool):
    boards = []
    conflictTotal = 0
    for i in range(8):
        if(elite == True):
            boards.append(b)
            elite = False
        else:
            tempBoard = Board(len(b.map))
            boards.append(tempBoard)
    #     print("Fitness:", boards[i].get_fitness())
    #     boards[i].show_map()
    # input("Enter to continue:")
    for i in range(len(boards)):
        conflictTotal += boards[i].get_fitness()
        geneStrand = ""
        for j in range(len(boards[i].map)):
            geneStrand += str(findQueen(boards[i], j))
        boards[i] = [geneStrand, boards[i].get_fitness()]
    return boards


def selection(b : Board, e):
    genePool = initialization(b, e)
    geneTotal = conflictTotal(genePool)
    geneAdder = 0
    for i in range(len(genePool)):
        if(i+1 == len(genePool)):
            genePool[i][1] = 1.0
            continue
        genePool[i][1] = geneAdder + (genePool[i][1]/geneTotal)
        geneAdder = genePool[i][1]
    winners = []
    for i in range(len(genePool)):
        seed = random.random()
        for j in range(len(genePool)):
            if(seed < genePool[j][1]):
                if(j == 0):
                    winners.append(genePool[j])
                    break
                else:
                    winners.append(genePool[j])
                    break
    return winners


def crossover(b : Board, e):
    arr = selection(b, e)
    for i in range(0, len(arr), 2):
        value1 = arr[i][0]
        value2 = arr[i+1][0]
        temp1 = ''
        temp2 = ''
        seed = random.randint(1, len(arr[0]))
        for j in range(seed):
            temp1 += arr[i][0][j]
            temp2 += arr[i+1][0][j]
            value1 = value1[1:]
            value2 = value2[1:]
        value1 = temp2 + value1
        value2 = temp1 + value2
        arr[i][0] = value1
        arr[i+1][0] = value2
    return arr


def mutation(b : Board, e):
    cross = crossover(b, e)
    for i in range(len(cross)):
        value = cross[i][0]
        seedIndex = random.randint(0, len(cross[i])-1)
        seedValue = random.randint(1, len(b.map))
        value = value[:seedIndex] + str(seedValue) + value[seedIndex+1:]
        cross[i][0] = value
    return cross


def specimens(b: Board, e):
    # print()
    finalBoards : Board = []
    best = comb(len(b.map), 2)
    bestBoard = Board(0)
    newBoard = mutation(b, e)
    for i in range(len(newBoard)):
        board = nullBoard(Board(len(b.map)))
        for j in range(len(b.map)):
            queens = newBoard[i][0]
            board.map[j][int(queens[j])-1] = 1
        finalBoards.append(board)
        # print("Fitness:", finalBoards[i].get_fitness())
        # finalBoards[i].show_map()
        if(best > finalBoards[i].get_fitness()):
            bestBoard = finalBoards[i]
            best = bestBoard.get_fitness()
    # print("New best fitness:", bestBoard.get_fitness())
    # bestBoard.show_map()
    # time.sleep(2)
    # print('b:')
    # b.show_map()
    # print("bB:")
    # bestBoard.show_map()
    if(bestBoard.get_fitness() > b.get_fitness()):
        return b
    else:
        return bestBoard


def naturalSelection(b : Board, winCond = 0):
    elitism = False
    topDog = specimens(b, elitism)
    elitism = True
    while(topDog.get_fitness() != winCond):
        topDog = specimens(topDog, elitism)
        # print("topDpg's fitness:", topDog.get_fitness())
        # topDog.show_map()
        # input("Enter:")
    return topDog


def displayBoard(b : Board):
    for i in range(len(b.map)):
        for j in range(len(b.map)):
            if(b.map[i][j] == 0):
                b.map[i][j] = '-'
            print(b.map[i][j], end=" ")
        print()
    return b




if __name__ == "__main__":
    # k = int(sys.argv[1])
    k = 5
    b = Board(k)
    darwin = Board(k)
    start_time = time.time()
    if(k == 3):
        darwin = naturalSelection(b, 1)
    elif(k > 3):
        darwin = naturalSelection(b)
    endTime = ((time.time() - start_time))*1000
    print(f"Running time: {int(endTime)}ms")
    displayBoard(darwin)