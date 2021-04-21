import copy
class Board:
    def _init_(self, startState, goalState, emptyIndex, priority=-1):
        self.startState = startState
        self.goalState = goalState
        self.emptyIndex = emptyIndex
        self.priority = priority

    def setPriority(self, priority):
        self.priority = priority

    def up(self):
        if self.emptyIndex[0] in range(1, 3) and self.emptyIndex[1] in range(0, 3):
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]
                                                ] = self.startState[self.emptyIndex[0]-1][self.emptyIndex[1]]
            self.startState[self.emptyIndex[0]-1][self.emptyIndex[1]] = 0
            self.emptyIndex = [self.emptyIndex[0]-1, self.emptyIndex[1]]
            return True
        else:
            return False

    def down(self):
        if self.emptyIndex[0] in range(0, 2) and self.emptyIndex[1] in range(0, 3):
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]
                                                ] = self.startState[self.emptyIndex[0]+1][self.emptyIndex[1]]
            self.startState[self.emptyIndex[0]+1][self.emptyIndex[1]] = 0
            self.emptyIndex = [self.emptyIndex[0]+1, self.emptyIndex[1]]
            return True
        else:
            return False

    def left(self):
        if self.emptyIndex[0] in range(0, 3) and self.emptyIndex[1] in range(1, 3):
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]
                                                ] = self.startState[self.emptyIndex[0]][self.emptyIndex[1]-1]
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]-1] = 0
            self.emptyIndex = [self.emptyIndex[0], self.emptyIndex[1]-1]
            return True
        else:
            return False

    def right(self):
        if self.emptyIndex[0] in range(0, 3) and self.emptyIndex[1] in range(0, 2):
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]
                                                ] = self.startState[self.emptyIndex[0]][self.emptyIndex[1]+1]
            self.startState[self.emptyIndex[0]][self.emptyIndex[1]+1] = 0
            self.emptyIndex = [self.emptyIndex[0], self.emptyIndex[1]+1]
            return True
        else:
            return False

    def isGoal(self):
        if self.startState == self.goalState:
            return True
        else:
            return False


pq = {}
visited = []


def heuristic(board):
    mismatchedTiles = 0
    for i in range(len(board.startState)):
        for j in range(len(board.startState[i])):
            if board.startState[i][j] != board.goalState[i][j]:
                mismatchedTiles += 1
    board.setPriority(mismatchedTiles)


def sortPq(pq):
    return sorted(pq)


def notVisited(currState):
    if currState in visited:
        return False
    else:
        return True


def hillClimbing(board):
    keyspq = []
    heuristic(board)
    pq[board.priority] = board
    keyspq = sortPq(pq)
    currState = pq.pop(keyspq[0])
    visited.append(currState.startState)
    i = 0
    while currState.startState != currState.goalState:
        i += 1

        if not notVisited(currState.startState):
            print(i, currState.startState)

        if currState.isGoal():
            print(f'Goal Reached')
            print(f'Current State : {currState.startState}')
            print(f'Goal State : {currState.goalState}')
            break

        upState = copy.deepcopy(currState)
        possible = upState.up()
        heuristic(upState)
        if possible and notVisited(upState.startState):
            pq[upState.priority] = upState

        else:
            del upState

        downState = copy.deepcopy(currState)
        possible = downState.down()
        heuristic(downState)
        if possible and notVisited(downState.startState):
            pq[downState.priority] = downState

        else:
            del downState

        leftState = copy.deepcopy(currState)
        possible = leftState.left()
        heuristic(leftState)
        if possible and notVisited(leftState.startState):
            pq[leftState.priority] = leftState

        else:
            del leftState

        rightState = copy.deepcopy(currState)
        possible = rightState.right()
        heuristic(rightState)
        if possible and notVisited(rightState.startState):
            pq[rightState.priority] = rightState

        else:
            del rightState

        keyspq = sortPq(pq)
        minHeuristicState = pq[keyspq[0]]

        if minHeuristicState.priority < currState.priority:
            visited.append(minHeuristicState.startState)
            currState = minHeuristicState
            keyspq.clear()
            pq.clear()
        else:
            print('Solution not possible using Hill Climbing Search')
            exit(0)

    print(f'{i+1} {currState.startState}')
    print(f'Goal Reached')
    print(f'Current State : {currState.startState}')
    print(f'Goal State : {currState.goalState}')


if _ _name_ _== '_ _main_ _':
    startState = [[2, 8, 3],
                  [1, 5, 0],
                  [7, 6, 4]]
    goalState = [[1, 2, 3],
                 [8, 0, 4],
                 [7, 6, 5]]

    board = Board(startState, goalState, [1, 2])

    print('Hill Climbing Search : ')
    hillClimbing(board)
