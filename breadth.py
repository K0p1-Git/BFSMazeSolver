#!/usr/bin/env python3
import queue, time
from colorama import init, Fore, Back, Style

## Preset Colors for the maze
COLOR_END       = Style.RESET_ALL               ## RESET/END
COLOR_GREEN     = Fore.GREEN + Style.BRIGHT     ## START
COLOR_RED       = Fore.RED + Style.BRIGHT       ## END
COLOR_YELLOW    = Fore.YELLOW + Style.BRIGHT    ## PATH
COLOR_CYAN      = Fore.CYAN + Style.BRIGHT      ## WALL

## createMaze() is a function that creates a 9x9 2D maze.
## It returns the list maze[] as well as the starting position of the maze
##
## --- Legend -------Constraints---
## Start    = O  |  Starting position can only be anywhere within maze[0].
## End      = X  |  Any where after maze[0].
## Wall     = #  |  Maze must be walled off.
##

def createMaze():
    maze = []
    startPos = [] 
    maze.append(['#','#', '#', '#', '#', '#','#','O','#'])   ## Have to start within this row
    maze.append(['#',' ', '#', ' ', ' ', ' ',' ',' ','#'])
    maze.append(['X',' ', '#', '#', ' ', '#','#',' ','#'])
    maze.append(['#',' ', '#', '#', ' ', ' ',' ',' ','#'])
    maze.append(['#',' ', ' ', '#', ' ', '#','#',' ','#'])
    maze.append(['#',' ', ' ', ' ', ' ', '#','#',' ','#'])
    maze.append(['#',' ', ' ', ' ', ' ', ' ',' ',' ','#'])
    maze.append(['#',' ', ' ', ' ', ' ', ' ','#',' ','#'])
    maze.append(['#','#', '#', '#', '#', '#','#','#','#'])
    
    ## Finding the starting position from the first row of the maze.

    for index, value in enumerate(maze[0]):
        if value == 'O': 
            startPos = index

    return maze, startPos

## visualizeMaze() is a function that prints out the final path the algorithm has chosen

def visualizeMaze(maze, moves):
    for row, col in enumerate(maze):
        for index, value in enumerate(col):
            if (row, index) in moves:               ## If the current row && index matches a set found in moves
                if value == 'X':                    ## it will print out '@' else it will print out the maze.    
                    print(COLOR_RED + value + ' ', end='')
                else:
                    print(COLOR_YELLOW + '@ ', end='')
            else:
                if value == 'O':
                    print(COLOR_GREEN + value + ' ', end='')
                else:
                    print(COLOR_CYAN + value + ' ', end='')
        print()

## solve() is a function that tries to solve the maze by using valid paths
## For each iteration from the main() function, a valid paths would be passed on to this function to test
## If the given path reaches the end goal of 'X' the solve function will stop and print out that specific path
## and also calling the visualizeMaze() function to print out the maze with the selected path.
##

def solve(maze, startPos, path):
    row = 0
    col = startPos
    moves = set()

    for move in path:
        if move == 'L':
            col -= 1
        elif move == 'R':
            col += 1
        elif move == 'U':
            row -= 1
        elif move == 'D':
            row += 1
        moves.add((row, col))

    if maze[row][col] == 'X':
        print(COLOR_GREEN + '\nFound: ' + path + '\n')
        visualizeMaze(maze, moves)
        return True
    return False

## valid() is a function that checks whether a given path is valid.
## Valid is defined by two constraint
##  
##  1) The path does not exit the boundary of the given maze
##  2) The path does not lead towards a wall, wall is defined as a '#'
##
## Once the given path has been tested, the valid() function will return
## 
##  True    = valid path
##  False   = invalid path
##

def valid(maze, startPos, path):
    row = 0
    col = startPos

    for move in path:
        if move == 'L':
            col -= 1
        elif move == 'R':
            col += 1
        elif move == 'U':
            row -= 1
        elif move == 'D':
            row += 1

    if not (0 <= col < len(maze[0]) and 0 <= row < len(maze)):
        return False
    elif maze[row][col] == '#':
        return False

    return True

## main() is a function uses the Breadth-first search (BFS) Algorithm to solve mazes.
## BFS is able to find the shortest path within a given maze and this program will demostrate this.
##

def main():
    start = time.time()
    q = queue.Queue()
    q.put('')
    add = ''
    maze, startPos = createMaze()
    index = 0

    while not solve(maze, startPos, add):
        add = q.get()
        index += 1
        print(COLOR_YELLOW +f'Attempt {index}: '+COLOR_RED + add)
        for direction in  ['L','R','U','D']:
            path = add + direction              ## Continue to add in four new possible direction it can take.
            if valid(maze, startPos, path):     ## Check to see if the direction is valid.
                q.put(path)                     ## If else, append this iteration into the queue. Else, drop it.

    print(COLOR_GREEN + f'\nTime Elapsed: {time.time() - start:.2f} seconds\n')
if __name__ == '__main__':
    main()
