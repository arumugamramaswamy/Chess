import numpy

class chessboard:

    def __init__(self):

        self.board = [["X" for x in range(8)]for x in range(8)]
        self.dictionary=dict()
         
        for g in range(8):
            self.board[1][g] = Pawn("B"+str(g+1),"w","wp"+str(g+1))
        for h in range(8):
            self.board[6][h] = Pawn("G"+str(g+1),"b","bp"+str(g+1))

        self.board[0][0] = Rook("A1","w","wr1")
        self.board[0][7] = Rook("A8","w","wr2")
        self.board[0][6] = Knight("A7","w","wk2")
        self.board[0][1] = Knight("A2","w","wk1")
        self.board[0][2] = Bishop("A3","w","wb1")
        self.board[0][5] = Bishop("A6","w","wb2")
        self.board[0][3] = Queen("A4","w","wq1")
        self.board[0][4] = King("A5","w"," w+")
        self.board[7][0] = Rook("H1","b","br1")
        self.board[7][7] = Rook("H8","b","br2")
        self.board[7][1] = Knight("H2","b","bk1")
        self.board[7][2] = Bishop("H3","b","bb1")
        self.board[7][3] = Queen("H4","b","bq1")
        self.board[7][4] = King("H5","b"," b+")
        self.board[7][5] = Bishop("H6","b","bb2")
        self.board[7][6] = Knight("H7","b","bk2")

        for x in range(8):
            for y in range(8):
                self.dictionary[str(str(chr(x+65))+str(y+1))]=self.board[x][y]

        self.board_as_matrix = self.print_board() 
    
    def print_board(self):
        board = [["X" for x in range(8)]for x in range(8)]
        for x in range(8):
            for y in range(8):
                if self.board[x][y]!="X":
                    board[x][y] = self.board[x][y].name
                else:
                    board[x][y] = ".X."
        board = numpy.array(board)
        print(board)
        return(board)

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

if __name__ == "__main__":
    a= chessboard()
