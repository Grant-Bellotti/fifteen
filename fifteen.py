# author: Grant Bellotti
# date: March 17th, 2023
# file: fifteen.py a Python program that allows users to play the fifteen puzzle game
# input: user responses (strings)
# output: interactive text messages and a board
import numpy as np
class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.size = size

    # gets the tile values
    def get_tiles(self):
        return self.tiles
    
    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        board = '+---+---+---+---+'
        for i in range(self.size):
            i += 1
            board += '\n|'
            for j in range((i-1)*self.size, i*self.size):
                if len(str(self.tiles[j])) == 1 and self.tiles[j] != 0:
                    board += f' {self.tiles[j]} |'
                elif len(str(self.tiles[j])) == 2 and self.tiles[j] != 0:
                    board += f'{self.tiles[j]} |'
                else:
                    board += f'   |'
            board += '\n+---+---+---+---+'
        print(board)

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self): 
        board = ''
        for i in range(self.size):
            i += 1
            for j in range((i-1)*self.size, i*self.size):
                if len(str(self.tiles[j])) == 1 and self.tiles[j] != 0:
                    board += f' {self.tiles[j]} '
                elif len(str(self.tiles[j])) == 2 and self.tiles[j] != 0:
                    board += f'{self.tiles[j]} '
                else:
                    board += f'   '
            board += '\n'
        return board

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        num1, num2 = self.tiles[i], self.tiles[j]
        self.tiles[i] = num2
        self.tiles[j] = num1

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        move = int(np.where(self.tiles == move)[0])
        if move+1 < len(self.tiles):
            if self.tiles[move+1] == 0 and move != 3 and move != 7 and move != 11:
                return True
        if move-1 >= 0:
            if self.tiles[move-1] == 0 and move != 4 and move != 8 and move != 12:
                return True
        if move+4 < len(self.tiles):
            if self.tiles[move+4] == 0:
                return True
        if move-4 >= 0:
            if self.tiles[move-4] == 0:
                return True
        return False


    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move): 
        swapIndex = -1
        isValid = self.is_valid_move(move)
        if isValid:
            move = int(np.where(self.tiles == move)[0])
            if move+1 < len(self.tiles):
                if self.tiles[move+1] == 0 and move != 3 and move != 7 and move != 11:
                    swapIndex = (move+1)
            if move-1 >= 0:
                if self.tiles[move-1] == 0 and move != 4 and move != 8 and move != 12:
                    swapIndex = (move-1)
            if move+4 < len(self.tiles):
                if self.tiles[move+4] == 0:
                    swapIndex = (move+4)
            if move-4 >= 0:
                if self.tiles[move-4] == 0:
                    swapIndex = (move-4)
            self.transpose(move, swapIndex)
    
    # shuffle tiles
    def shuffle(self, moves = 100):
        np.random.shuffle(self.tiles)
    
    # verify if the puzzle is solved
    def is_solved(self):
        testVals = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        return ((self.tiles == testVals).all())

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass

if __name__ == '__main__':
    """game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    game.draw()
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False"""
    
    
    '''You should be able to play the game if you uncomment the code below'''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    