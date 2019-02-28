import numpy

class chessboard:

    def __init__(self):
        self.board = [["X" for x in range(8)]for x in range(8)]
        self.dictionary=dict()
        for g in range(8):
            self.board[1][g] = "wp"
        for h in range(8):
            self.board[6][h] = "bp"
        self.board[0][0] = "wr"
        self.board[0][7] = "wr"
        self.board[0][6] = "wk"
        self.board[0][1] = "wk"
        self.board[0][2] = "wb"
        self.board[0][5] = "wb"
        self.board[0][3] = "wq"
        self.board[0][4] = "w+"
        self.board[7][0] = "br"
        self.board[7][7] = "br"
        self.board[7][1] = "bk"
        self.board[7][2] = "bb"
        self.board[7][3] = "bq"
        self.board[7][4] = "b+"
        self.board[7][5] = "bb"
        self.board[7][6] = "bk"
        for x in range(8):
            for y in range(8):
                print(type(self.dictionary))
                self.dictionary[str(str(chr(x+65))+str(y+1))]=self.board[x][y]
    
    def print_board(self):
        board = numpy.array(self.board)
        print(board)

class Pawn:
    
    def __init__(self, start_loc, color, name):
        self.d_step= True
        self.loc = start_loc
        # check for en-pasant
        self.emp = False
        self.color = color
        self.name = name

    def d_step(self):
        # self.loc +=2 or self.loc-=2
        self.emp = True
        self.d_step = False
        
        if self.color == "b":
            self.loc-=2
        else:  
            self.loc+=2
    
    def move(self):
        self.d_step = False
        # self.loc +=1 or self.loc-=1
        if self.color == "b":
            self.loc-=1
        else:  
            self.loc+=1
        
        if self.loc == 8 and self.color=="b":
            self.promote()
        elif self.loc == 1 and self.color=="w":
            self.promote()

    
    def capture(self,final_location):
        self.d_step = False
        # cut in appropriate direction

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass
        
    def promote(self):
        #promote
        pass

class Rook:
    
    def __init__(self, start_loc, color, name):
        self.castle= True
        self.loc = start_loc
        self.color = color
        self.name = name

    def castle(self):
        self.castle = False
        # needs to perform castle
        
    def move(self,final_location):
        self.castle = False
        # move to location
    
    def capture(self,final_location):
        self.castle = False
        # pretty much move

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass
        
class King:

    def __init__(self, start_loc, color, name):
        self.castle= True
        self.loc = start_loc
        self.color = color
        self.name = name

    def castle(self):
        self.castle = False
        # needs to perform castle
        
    def move(self,final_location):
        self.castle = False
        # move to location
    
    def capture(self,final_location):
        self.castle = False
        # pretty much move

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass
        
class Queen:

    def __init__(self, start_loc, color, name):
        self.loc = start_loc
        self.color = color
        self.name = name
        
    def move(self,final_location):
        # move to location
        pass
    
    def capture(self,final_location):
        # pretty much move
        pass

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

class Bishop:

    def __init__(self, start_loc, color, name):
        self.loc = start_loc
        self.color = color
        self.name = name
        
    def move(self,final_location):
        # move to location
        pass

    def capture(self,final_location):
        # pretty much move
        pass

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

class Knight:

    def __init__(self, start_loc, color, name):
        self.loc = start_loc
        self.color = color
        self.name = name
        
    def move(self,final_location):
        # move to location
        pass
    
    def capture(self,final_location):
        # pretty much move
        pass
    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

a= chessboard()
a.print_board()