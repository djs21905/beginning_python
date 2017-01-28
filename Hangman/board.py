# Class for drawing the Game Board 

class Board():

        board = []
        initialize = True 

        def __init__(self, size):

                self.board_size = size 
  
        def drawBoard(self, index_of_spaces):
                Board.board
                board_space = '_'
                
                for spaces in range(self.board_size):
                         Board.board.append(board_space)

                for index in index_of_spaces:
                        Board.board[index] = ' ' 

                print('\n' * 200 + ''.join(Board.board), end= '')                   
                return Board.board

        def updateBoard(self, mysteryword, guess):
                list_mysteryword = list(mysteryword)
                for index , char in  enumerate(list_mysteryword):
                        if char == guess: 
                                Board.board[index] =  guess 
                print(''.join(Board.board), end= '')                   
                return Board.board        


                       









