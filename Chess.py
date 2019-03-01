import numpy

# returns matrix coords from chess loc
def retrieve_x_y(string):
    return [ord(string[0])-65,int(string[1])-1]

# returns chess loc from matrix coords
def retrieve_loc(x_y):
    return str(chr(x_y[0]+65)+str(x_y[1]+1))

# helps in reusing code
def move_maker(piece,x_y_new):
    piece.chessboard.dictionary[piece.loc] = "X"
    temp = piece.chessboard.board[piece.x_y[0]][piece.x_y[1]]
    piece.chessboard.board[piece.x_y[0]][piece.x_y[1]] = "X"
    piece.x_y[0] = x_y_new[0]
    piece.x_y[1] = x_y_new[1]
    piece.chessboard.board[piece.x_y[0]][piece.x_y[1]]=temp
    piece.chessboard.dictionary[piece.loc] = temp

class chessboard:

    def __init__(self):
        # self.board stores the piece objects
        self.board = [["X" for x in range(8)]for x in range(8)]
        self.dictionary=dict()

        
        # setting up the board
        for g in range(8):
            exec('''self.board[1][g] = wp'''+str(g+1)+''' =Pawn("B"+str(g+1),"w","wp"+str(g+1),self)''')
        for h in range(8):
            exec('''self.board[6][h] = bp'''+str(g+1)+''' =Pawn("G"+str(h+1),"b","bp"+str(h+1),self)''')
        
        wp1 = self.board[1][0]
        wp2 = self.board[1][1]
        wp3 = self.board[1][2]
        wp4 = self.board[1][3]
        wp5 = self.board[1][4]
        wp6 = self.board[1][5]
        wp7 = self.board[1][6]
        wp8 = self.board[1][7]

        bp1 = self.board[7][0]
        bp2 = self.board[7][1]
        bp3 = self.board[7][2]
        bp4 = self.board[7][3]
        bp5 = self.board[7][4]
        bp6 = self.board[7][5]
        bp7 = self.board[7][6]
        bp8 = self.board[7][7]

        self.board[0][0] = wr1 = Rook("A1", "w", "wr1", self)
        self.board[0][7] = wr2 = Rook("A8", "w", "wr2", self)
        self.board[0][6] = wk2 = Knight("A7", "w", "wk2", self)
        self.board[0][1] = wk1 = Knight("A2", "w", "wk1", self)
        self.board[0][2] = wb1 = Bishop("A3", "w", "wb1", self)
        self.board[0][5] = wb2 = Bishop("A6", "w", "wb2", self)
        self.board[0][3] = wq1 = Queen("A4", "w", "wq1", self)
        self.board[0][4] = self.wki = King("A5", "w", "w+ ", self)
        self.board[7][0] = br1 = Rook("H1", "b", "br1", self)
        self.board[7][7] = br2 = Rook("H8", "b", "br2", self)
        self.board[7][1] = bk1 = Knight("H2", "b", "bk1", self)
        self.board[7][2] = bb1 = Bishop("H3", "b", "bb1", self)
        self.board[7][3] = bq1 = Queen("H4", "b", "bq1", self)
        self.board[7][4] = self.bki = King("H5", "b", "b+ ", self)
        self.board[7][5] = bb2 = Bishop("H6", "b", "bb2", self)
        self.board[7][6] = bk2 = Knight("H7", "b", "bk2", self)

        #test piece
        #self.board[2][0]= wr3 = Rook("C1", "w", "wr3", self)

        self.white_piece_list = [wr1,wr2,wk1,wk2,wb1,wb2,wq1,wki,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]
        self.black_piece_list = [br1,br2,bk1,bk2,bb1,bb2,bq1,bki,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
        
        self.piece_list = self.white_piece_list + self.black_piece_list

        # self.dictionary contains all the piece objects stored against location(in chess notation)
        # it also stores the matrix x,y coords 

        for x in range(8):
            for y in range(8):
                self.dictionary[str(str(chr(x+65))+str(y+1))]=[self.board[x][y],[x,y]]

        # storing the board in an easily prontable form(without objects)

        self.board_as_matrix = self.print_board() 

        self.white_pawns = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]
        self.black_pawns = [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
    
    # returns the board as a matrix(without objects) and also prints

    def print_board(self):
        board = [["X" for x in range(8)]for x in range(8)]
        for x in range(8):
            for y in range(8):
                if self.board[x][y]!="X":
                    board[x][y] = self.board[x][y].name
                else:
                    board[x][y] = ".X."
        boarda = numpy.array(board)
        print(boarda)
        return(board)

    def remove_piece(self,piece):
        pass

    def move(self):
        pass

class Pawn():
    
    def __init__(self, start_loc, color, name, chessboard):

        # sets a flag to check whether a pawn can double step  
        self.d_step= True

        # assigning location in chess notation
        self.loc = start_loc

        # assigning location in matrix format
        self.x_y = retrieve_x_y(self.loc)

        # flag for en-pasant
        self.emp = False

        # color of the piece
        self.color = color

        # name of the piece - mainly for printing
        self.name = name

        # copy of current chessboard
        self.chessboard = chessboard

    def move_d_step(self):

        if self.d_step == True:

            # setting en pasant flag to true (will be set to false after one turn)
            self.emp = True

            # setting double step flag to false
            self.d_step = False
            
            # checking for obstructions
            if self.color == "b" and self.chessboard.board[self.x_y[0]-1][self.x_y[1]]=="X" and self.chessboard.board[self.x_y[0]-2][self.x_y[1]]=="X":
                
                # IMPORTANT - copy current board state and at the end of move, check for kcheck 
                # if True reset and return invalid

                # making the move
                move_maker(self,[self.x_y[0]-2,self.x_y[1]])

            elif self.color == "w" and self.chessboard.board[self.x_y[0]+1][self.x_y[1]]=="X" and self.chessboard.board[self.x_y[0]+2][self.x_y[1]]=="X":  
                
                # IMPORTANT - copy current board state and at the end of move, check for kcheck 
                # if True reset and return invalid

                # making the move
                move_maker(self,[self.x_y[0]+2,self.x_y[1]])


            else:
                print("invalid move")
                self.emp = False
                self.d_step = True

            self.loc = retrieve_loc(self.x_y)
        
        else:
            print("invalid move")
        
        return self.chessboard
    
    def move(self):
        dstep = self.d_step
        self.d_step = False
        if self.color == "b" and self.chessboard.board[self.x_y[0]-1][self.x_y[1]]=="X":

            # IMPORTANT - copy current board state and at the end of move, check for kcheck 
            # if True reset and return invalid

            # making the move
            move_maker(self,[self.x_y[0]-1,self.x_y[1]])


        elif self.color == "w" and self.chessboard.board[self.x_y[0]+1][self.x_y[1]]=="X":  

            # IMPORTANT - copy current board state and at the end of move, check for kcheck 
            # if True reset and return invalid

            # making the move
            move_maker(self,[self.x_y[0]+1,self.x_y[1]])

        else:
            print("invalid move")
            self.d_step = dstep
        
        self.loc = retrieve_loc(self.x_y)

        # promtions
        if self.x_y[0] == 7 and self.color=="b":
            self.promote()
        elif self.x_y[0] == 0 and self.color=="w":
            self.promote()

        return self.chessboard

    # first checks for piece colour
    # if white:
    # 1) checks for right end of board
    # 2) if True skips over
    # 3) if not right board end also references final location and existance of a black piece at attack location
    # 4) 1-3 repeated for left board end in elif
    # if black:
    # 1-4 repeated for black

    def capture(self,final_location):
        self.d_step = False
        attack_matrix = self.generate_attack_matrix(self)
        if self.color == "w":
    

            if self.x_y[1]!=7 and self.chessboard[self.x_y[0]+1][self.x_y[1]+1].color == "b" and final_location == retrieve_loc([self.x_y[0]+1,self.x_y[1]+1]):
                move_maker(self,[self.x_y[0]+1,self.x_y[1]+1])

            elif self.x_y[1]!=0 and self.chessboard[self.x_y[0]+1][self.x_y[1]-1].color == "b" and final_location == retrieve_loc([self.x_y[0]+1,self.x_y[1]-1]):
                move_maker(self,[self.x_y[0]+1,self.x_y[1]-1])

            else:
                print("invalid move")
                
        elif self.color == "b":
            
            if self.x_y[1]!=0 and self.chessboard[self.x_y[0]-1][self.x_y[1]-1].color == "w" and final_location == retrieve_loc([self.x_y[0]-1,self.x_y[1]-1]):
                
                move_maker(self,[self.x_y[0]-1,self.x_y[1]-1])
            
            elif self.x_y[1]!=7 and self.chessboard[self.x_y[0]-1][self.x_y[1]+1].color == "w" and final_location == retrieve_loc([self.x_y[0]-1,self.x_y[1]+1]):
                
                move_maker(self,[self.x_y[0]-1,self.x_y[1]+1])
            
            else:
                print("invalid move")

        self.loc = retrieve_loc(self.x_y)

        # promotions
        if self.x_y[0] == 7 and self.color=="b":
            self.promote()
        elif self.x_y[0] == 0 and self.color=="w":
            self.promote()

        return self.chessboard

    # needs to generate the places of possible attack
        
    def generate_attack_matrix(self):
        
        attack_matrix = [[0 for x in range(8)] for y in range(8)]

        if self.color = "w":

            if self.x_y[1]!=7:
                attack_matrix[self.x_y[0]+1][self.x_y[1]+1] = 1
            if self.loc[1]!=0:
                attack_matrix[self.x_y[0]+1][self.x_y[1]-1] = 1

        else:

            if self.x_y[1]!=7:
                attack_matrix[self.x_y[0]-1][self.x_y[1]+1] = 1
            if self.x_y[1]!=0:
                attack_matrix[self.x_y[0]-1][self.x_y[1]-1] = 1
        
        return attack_matrix
        
    def promote(self):
        #promote
        pass

    def update(self,chessboard):
        self.chessboard = chessboard

class Rook:
    
    def __init__(self, start_loc, color, name, chessboard):
        self.castle= True
        self.loc = start_loc
        self.color = color
        self.name = name
        self.chessboard = chessboard
        self.x_y = retrieve_x_y(self.loc)

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

    def update(self,chessboard):
        self.chessboard = chessboard

class King:

    def __init__(self, start_loc, color, name, chessboard):
        self.castle= True
        self.loc = start_loc
        self.color = color
        self.name = name
        self.chessboard = chessboard
        self.x_y = retrieve_x_y(self.loc)

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
        
    def update(self,chessboard):
        self.chessboard = chessboard

class Queen:

    def __init__(self, start_loc, color, name, chessboard):
        self.loc = start_loc
        self.color = color
        self.name = name
        self.chessboard = chessboard
        self.x_y = retrieve_x_y(self.loc)
        
    def move(self,final_location):
        # move to location
        pass
    
    def capture(self,final_location):
        # pretty much move
        pass

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

    def update(self,chessboard):
        self.chessboard = chessboard

class Bishop:

    def __init__(self, start_loc, color, name, chessboard):
        self.loc = start_loc
        self.color = color
        self.name = name
        self.chessboard = chessboard
        self.x_y = retrieve_x_y(self.loc)
        
    def move(self,final_location):
        # move to location
        pass

    def capture(self,final_location):
        # pretty much move
        pass

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

    def update(self,chessboard):
        self.chessboard = chessboard

class Knight:

    def __init__(self, start_loc, color, name, chessboard):
        self.loc = start_loc
        self.color = color
        self.name = name
        self.chessboard = chessboard
        self.x_y = retrieve_x_y(self.loc)
        
    def move(self,final_location):
        # move to location
        pass
    
    def capture(self,final_location):
        # pretty much move
        pass

    def generate_attack_matrix(self,chessboard):
        # needs to generate the places of possible attack
        pass

    def update(self,chessboard):
        self.chessboard = chessboard

if __name__ == "__main__":
    a= chessboard()
