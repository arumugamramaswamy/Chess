import numpy
from copy import deepcopy

def piece_possible_moves(piece):
    hypothetical_moves_list,hypothetical_capture_list = return_hypothetical_moves_list(piece)

    temp_piece = deepcopy(piece)
    temp_piece_chessboard = deepcopy(piece.chessboard)

    possible_moves = []
    possible_captures = []

    if piece.color == "w":
        
        for temp_x_y in hypothetical_moves_list:
            temp_piece.move(retrieve_loc(temp_x_y))
            
            check = temp_piece.chessboard.wki.check_for_check()
            if not check:
                possible_moves.append(temp_x_y)
            temp_piece = deepcopy(piece)
            temp_piece.chessboard = deepcopy(piece.chessboard)
        
        for temp_x_y in hypothetical_capture_list:
            temp_piece.capture(retrieve_loc(temp_x_y))
            check = temp_piece.chessboard.wki.check_for_check()
            if not check:
                possible_captures.append(temp_x_y)
            temp_piece = deepcopy(piece)
            temp_piece.chessboard = deepcopy(piece.chessboard)
    
    else:

        for temp_x_y in hypothetical_moves_list:
            temp_piece.move(retrieve_loc(temp_x_y))
            check = temp_piece.chessboard.bki.check_for_check()
            if not check:
                possible_moves.append(temp_x_y)
            temp_piece = deepcopy(piece)
            temp_piece.chessboard = deepcopy(piece.chessboard)
        
        for temp_x_y in hypothetical_capture_list:
            temp_piece.capture(retrieve_loc(temp_x_y))
            check = temp_piece.chessboard.bki.check_for_check()
            if not check:
                possible_captures.append(temp_x_y)
            temp_piece = deepcopy(piece)
            temp_piece.chessboard = deepcopy(piece.chessboard)

    return possible_moves, possible_captures

# doesn't apply for pawns due to multiple types of moves

def return_hypothetical_moves_list(piece):

    attack_matrix = piece.generate_attack_matrix()
    hypothetical_moves_list = []
    hypothetical_capture_list = []
    for x in range(8):
        for y in range(8):
            if attack_matrix[x][y]==1:
                if piece.chessboard.board[x][y].color=="X":
                    hypothetical_moves_list.append([x,y])
                elif piece.chessboard.board[x][y].color!=piece.color:
                    hypothetical_capture_list.append([x,y])

    
    return hypothetical_moves_list, hypothetical_capture_list

# returns matrix coords from chess loc

def retrieve_x_y(string):
    return [int(string[1])-1,ord(string[0])-65]

# returns chess loc from matrix coords

def retrieve_loc(x_y):
    return str(chr(x_y[1]+65)+str(x_y[0]+1))

class empty:

    def __init__(self):
        self.color = "X"
        self.name = ".X."

# helps in reusing code

def move_maker(piece,x_y_new):
    piece.chessboard.dictionary[piece.loc] = [empty(),retrieve_x_y(piece.loc)]
    temp = piece.chessboard.board[piece.x_y[0]][piece.x_y[1]]
    piece.chessboard.board[piece.x_y[0]][piece.x_y[1]] = empty()
    piece.x_y[0] = x_y_new[0]
    piece.x_y[1] = x_y_new[1]
    piece.loc = retrieve_loc(piece.x_y)
    piece.chessboard.board[piece.x_y[0]][piece.x_y[1]]=temp
    piece.chessboard.dictionary[piece.loc] = [temp,x_y_new]

class chessboard:

    def __init__(self):
        # self.board stores the piece objects
        self.board = [[empty() for x in range(8)]for x in range(8)]
        self.dictionary=dict()

        
        # setting up the board
        for g in range(8):
            exec('''self.board[1][g] = wp'''+str(g+1)+''' =Pawn(chr(g+65)+"2","w","wp"+str(g+1),self)''')
        for h in range(8):
            exec('''self.board[6][h] = bp'''+str(g+1)+''' =Pawn(chr(h+65)+"7","b","bp"+str(h+1),self)''')
        
        wp1 = self.board[1][0]
        wp2 = self.board[1][1]
        wp3 = self.board[1][2] = empty()
        wp4 = self.board[1][3]
        wp5 = self.board[1][4]
        wp6 = self.board[1][5]
        wp7 = self.board[1][6]
        wp8 = self.board[1][7]
        #wr3 = self.board[3][4] = Rook("E4","w","wr3",self)
        bb3 = self.board[3][0] = Bishop("A4","b","bb3",self)

        bp1 = self.board[6][0]
        bp2 = self.board[6][1]
        bp3 = self.board[6][2]
        bp4 = self.board[6][3]
        bp5 = self.board[6][4]
        bp6 = self.board[6][5]
        bp7 = self.board[6][6]
        bp8 = self.board[6][7]
        
        #self.board[5][5] = wk3 = Knight(retrieve_loc([5,5]),"w","wk3",self)
        
        self.board[0][0] = wr1 = Rook("A1", "w", "wr1", self)
        self.board[0][7] = wr2 = Rook("H1", "w", "wr2", self)
        self.board[0][6] = wk2 = Knight("G1", "w", "wk2", self)
        #self.board[0][1] = wk1 = Knight("B1", "w", "wk1", self)
        #self.board[0][2] = wb1 = Bishop("C1", "w", "wb1", self)
        self.board[0][5] = wb2 = Bishop("F1", "w", "wb2", self)
        #self.board[0][3] = wq1 = Queen("D1", "w", "wq1", self)
        self.board[0][4] = self.wki = King("E1", "w", "w+ ", self)
        self.board[7][0] = br1 = Rook("A8", "b", "br1", self)
        self.board[7][7] = br2 = Rook("H8", "b", "br2", self)
        self.board[7][1] = bk1 = Knight("B8", "b", "bk1", self)
        self.board[7][2] = bb1 = Bishop("C8", "b", "bb1", self)
        self.board[7][3] = bq1 = Queen("D8", "b", "bq1", self)
        self.board[7][4] = self.bki = King("E8", "b", "b+ ", self)
        self.board[7][5] = bb2 = Bishop("F8", "b", "bb2", self)
        self.board[7][6] = bk2 = Knight("G8", "b", "bk2", self)

        #test piece
        #self.board[2][0]= wr3 = Rook("C1", "w", "wr3", self)

        self.white_piece_list = [wr1,wr2,wk2,wb2,self.wki,wp1,wp2,wp4,wp5,wp6,wp7,wp8]#,wk1,wb1,wq1,wp3]
        self.black_piece_list = [br1,br2,bk1,bk2,bb1,bb2,bq1,self.bki,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bb3]

        
        
        self.piece_list = self.white_piece_list + self.black_piece_list

        # self.dictionary contains all the piece objects stored against location(in chess notation)
        # it also stores the matrix x,y coords 

        for x in range(8):
            for y in range(8):
                self.dictionary[str(str(chr(y+65))+str(x+1))]=[self.board[x][y],[x,y]]

        # storing the board in an easily prontable form(without objects)

        self.board_as_matrix = self.print_board() 

        self.white_pawns = [wp1,wp2,wp4,wp5,wp6,wp7,wp8]#,wp3]
        self.black_pawns = [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]



        self.w_queen_counter = 1
        self.b_queen_counter = 1
        self.w_knight_counter = 2
        self.b_knight_counter = 2
        self.w_rook_counter = 2
        self.b_rook_counter = 2
        self.w_bishop_counter = 2
        self.b_bishop_counter = 2

    # returns the board as a matrix(without objects) and also prints

    def print_board(self):
        board = [["X" for x in range(8)]for x in range(8)]
        for x in range(8):
            for y in range(8):
                board[x][y] = self.board[x][y].name
        boarda = numpy.array(board)
        print(boarda)
        return(board)

    def remove_piece(self,piece):
        if piece.name[:2]=="wp":
            self.white_pawns.remove(piece)
            self.white_piece_list.remove(piece)
        elif piece.name[:2]=="bp":
            self.black_pawns.remove(piece)
            self.black_piece_list.remove(piece)
        elif piece.name[0]=="b":
            self.black_piece_list.remove(piece)
        elif piece.name[0]=="w":
            self.white_piece_list.remove(piece)

    def color_all_possible_moves(self,color):
        all_possible_moves = []
        all_possible_captures = []
        if color =="w":
            self.wki.no_of_moves = 0
            for piece in self.white_piece_list:
                all_possible_moves.append([piece.name,piece.return_possible_moves()[0]])
                self.wki.no_of_moves+=len(piece.return_possible_moves()[0])
                all_possible_captures.append([piece.name,piece.return_possible_moves()[1]])
                self.wki.no_of_moves+=len(piece.return_possible_moves()[1])
        else:
            self.bki.no_of_moves = 0
            for piece in self.black_piece_list:
                all_possible_moves.append([piece.name,piece.return_possible_moves()[0]])
                self.bki.no_of_moves+=len(piece.return_possible_moves()[0])
                all_possible_captures.append([piece.name,piece.return_possible_moves()[1]])
                self.bki.no_of_moves+=len(piece.return_possible_moves()[1])        
        return all_possible_moves,all_possible_captures

    def move(self,chess_notation):
        pass

class Pawn:
    
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
            if self.color == "b" and self.chessboard.board[self.x_y[0]-1][self.x_y[1]].color=="X" and self.chessboard.board[self.x_y[0]-2][self.x_y[1]].color=="X":
                
                # IMPORTANT - copy current board state and at the end of move, check for kcheck 
                # if True reset and return invalid

                # making the move
                move_maker(self,[self.x_y[0]-2,self.x_y[1]])

            elif self.color == "w" and self.chessboard.board[self.x_y[0]+1][self.x_y[1]].color=="X" and self.chessboard.board[self.x_y[0]+2][self.x_y[1]].color=="X":  
                
                # IMPORTANT - copy current board state and at the end of move, check for kcheck 
                # if True reset and return invalid

                # making the move
                move_maker(self,[self.x_y[0]+2,self.x_y[1]])

            else:
                print("1 invalid move")
                self.emp = False
                self.d_step = True

            self.loc = retrieve_loc(self.x_y)
        
        else:
            print("2 invalid move")
        
    def move_sub(self):
        dstep = self.d_step
        self.d_step = False
        if self.color == "b" and self.chessboard.board[self.x_y[0]-1][self.x_y[1]].color=="X":

            # IMPORTANT - copy current board state and at the end of move, check for kcheck 
            # if True reset and return invalid

            # making the move
            move_maker(self,[self.x_y[0]-1,self.x_y[1]])


        elif self.color == "w" and self.chessboard.board[self.x_y[0]+1][self.x_y[1]].color=="X":  

            # IMPORTANT - copy current board state and at the end of move, check for kcheck 
            # if True reset and return invalid

            # making the move
            move_maker(self,[self.x_y[0]+1,self.x_y[1]])

        else:
            print("3 invalid move")
            self.d_step = dstep
        
        self.loc = retrieve_loc(self.x_y)

        # promtions
        if self.x_y[0] == 7 and self.color=="b":
            self.promote()
        elif self.x_y[0] == 0 and self.color=="w":
            self.promote()

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
        attack_matrix = self.generate_attack_matrix()
        final_x_y = retrieve_x_y(final_location)
        if self.color == "w":
    

            if self.x_y[1]!=7 and self.chessboard.board[self.x_y[0]+1][self.x_y[1]+1].color == "b" and final_location == retrieve_loc([self.x_y[0]+1,self.x_y[1]+1]):
                
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,[self.x_y[0]+1,self.x_y[1]+1])

            elif self.x_y[1]!=0 and self.chessboard.board[self.x_y[0]+1][self.x_y[1]-1].color == "b" and final_location == retrieve_loc([self.x_y[0]+1,self.x_y[1]-1]):
                
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,[self.x_y[0]+1,self.x_y[1]-1])
            else:
                print("4 invalid move")
                
        elif self.color == "b":
            
            if self.x_y[1]!=0 and self.chessboard.board[self.x_y[0]-1][self.x_y[1]-1].color == "w" and final_location == retrieve_loc([self.x_y[0]-1,self.x_y[1]-1]):
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,[self.x_y[0]-1,self.x_y[1]-1])
                

            elif self.x_y[1]!=7 and self.chessboard.board[self.x_y[0]-1][self.x_y[1]+1].color == "w" and final_location == retrieve_loc([self.x_y[0]-1,self.x_y[1]+1]):
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,[self.x_y[0]-1,self.x_y[1]+1])
                

            else:
                print("5 invalid move")

        self.loc = retrieve_loc(self.x_y)

        # promotions
        if self.x_y[0] == 7 and self.color=="w":
            self.promote()
        elif self.x_y[0] == 0 and self.color=="b":
            self.promote()

    # needs to generate the places of possible attack
        
    def generate_attack_matrix(self):
        
        attack_matrix = [[0 for x in range(8)] for y in range(8)]

        if self.color == "w":

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
        
    # change dictionary values

    def promote(self):
        
        while True:

            promo = input("q/r/k/b")

            #promote to queen
            if promo == "q":
                if self.color == "w":
                    self.chessboard.remove_piece(self)
                    self.chessboard.white_piece_list.append(Queen(self.loc,self.color,self.color+"q"+str(self.chessboard.w_queen_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1]
                    self.chessboard.w_queen_counter+=1
                    self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1].chessboard = self.chessboard
                else:
                    self.chessboard.remove_piece(self)
                    self.chessboard.black_piece_list.append(Queen(self.loc,self.color,self.color+"q"+str(self.chessboard.b_queen_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1]
                    self.chessboard.b_queen_counter+=1
                    self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1].chessboard = self.chessboard
                break
            
            #promote to rook
            elif promo == "r":
                if self.color == "w":
                    self.chessboard.remove_piece(self)
                    self.chessboard.white_piece_list.append(Rook(self.loc,self.color,self.color+"q"+str(self.chessboard.w_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1]
                    self.chessboard.w_rook_counter+=1
                    self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1].chessboard = self.chessboard
                else:
                    self.chessboard.remove_piece(self)
                    self.chessboard.black_piece_list.append(Rook(self.loc,self.color,self.color+"q"+str(self.chessboard.b_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1]
                    self.chessboard.b_rook_counter+=1
                    self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1].chessboard = self.chessboard
                break

            #promote to knight            
            elif promo == "k":
                if self.color == "w":
                    self.chessboard.remove_piece(self)
                    self.chessboard.white_piece_list.append(Knight(self.loc,self.color,self.color+"q"+str(self.chessboard.w_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1]
                    self.chessboard.w_rook_counter+=1
                    self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1].chessboard = self.chessboard
                else:
                    self.chessboard.remove_piece(self)
                    self.chessboard.black_piece_list.append(Knight(self.loc,self.color,self.color+"q"+str(self.chessboard.b_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1]
                    self.chessboard.b_rook_counter+=1
                    self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1].chessboard = self.chessboard
                break

            #promote to bishop            
            elif promo == "b":
                if self.color == "w":
                    self.chessboard.remove_piece(self)
                    self.chessboard.white_piece_list.append(Bishop(self.loc,self.color,self.color+"q"+str(self.chessboard.w_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1]
                    self.chessboard.w_rook_counter+=1
                    self.chessboard.white_piece_list[len(self.chessboard.white_piece_list)-1].chessboard = self.chessboard
                else:
                    self.chessboard.remove_piece(self)
                    self.chessboard.black_piece_list.append(Bishop(self.loc,self.color,self.color+"q"+str(self.chessboard.b_rook_counter+1),self.chessboard))
                    self.chessboard.board[self.x_y[0]][self.x_y[1]] = self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1]
                    self.chessboard.b_rook_counter+=1
                    self.chessboard.black_piece_list[len(self.chessboard.black_piece_list)-1].chessboard = self.chessboard
                break

    def pawn_hypothetical_moves_list(self):
        hypothetical_moves_list = []
        hypothetical_capture_list = []
        attack_matrix = self.generate_attack_matrix()
        
        if self.color == "w":
            if self.chessboard.board[self.x_y[0]+1][self.x_y[1]].color == "X":
                hypothetical_moves_list.append([self.x_y[0]+1,self.x_y[1]])
                if self.d_step and self.chessboard.board[self.x_y[0]+2][self.x_y[1]].color == "X":
                    hypothetical_moves_list.append([self.x_y[0]+2,self.x_y[1]])
            if self.x_y[1]!=7 and self.chessboard.board[self.x_y[0]+1][self.x_y[1]+1].color == "b":
                hypothetical_capture_list.append([self.x_y[0]+1,self.x_y[1]+1])
            if self.x_y[1]!=0 and self.chessboard.board[self.x_y[0]+1][self.x_y[1]-1].color == "b":
                hypothetical_capture_list.append([self.x_y[0]+1,self.x_y[1]-1])
        
        elif self.color == "b":
            if self.chessboard.board[self.x_y[0]-1][self.x_y[1]].color == "X":
                hypothetical_moves_list.append([self.x_y[0]-1,self.x_y[1]])
                if self.d_step and self.chessboard.board[self.x_y[0]-2][self.x_y[1]].color == "X":
                    hypothetical_moves_list.append([self.x_y[0]-2,self.x_y[1]])
            if self.x_y[1]!=7 and self.chessboard.board[self.x_y[0]-1][self.x_y[1]+1].color == "w":
                hypothetical_capture_list.append([self.x_y[0]-1,self.x_y[1]+1])
            if self.x_y[1]!=0 and self.chessboard.board[self.x_y[0]-1][self.x_y[1]-1].color == "w":
                hypothetical_capture_list.append([self.x_y[0]-1,self.x_y[1]-1])

        return hypothetical_moves_list,hypothetical_capture_list

    def move(self,final_location):

        final_x_y = retrieve_x_y(final_location)
        if self.color =="w":
            if final_x_y==[self.x_y[0]+1,self.x_y[1]]:
                self.move_sub()
            elif final_x_y ==[self.x_y[0]+2,self.x_y[1]]:
                self.move_d_step()
            else:
                print("6 invalid move")
        elif self.color =="b":
            if final_x_y==[self.x_y[0]-1,self.x_y[1]]:
                self.move_sub()
            elif final_x_y ==[self.x_y[0]-2,self.x_y[1]]:
                self.move_d_step()
            else:
                print("7 invalid move")

    def return_possible_moves(self):

        hypothetical_moves_list, hypothetical_capture_list = self.pawn_hypothetical_moves_list()


        temp_self = deepcopy(self)
        temp_self_chessboard = deepcopy(self.chessboard)

        possible_moves = []
        possible_captures = []

        if self.color == "w":
            
            for temp_x_y in hypothetical_moves_list:
                temp_self.move(retrieve_loc(temp_x_y))
                #print(self.chessboard == temp_self.chessboard)
                check = temp_self.chessboard.wki.check_for_check()
                if not check:
                    possible_moves.append(temp_x_y)
                temp_self = deepcopy(self)
                temp_self_chessboard = deepcopy(self.chessboard)
            
            
            for temp_x_y in hypothetical_capture_list:
                temp_self.capture(retrieve_loc(temp_x_y))
                check = temp_self.chessboard.wki.check_for_check()
                if not check:
                    possible_captures.append(temp_x_y)
                temp_self = deepcopy(self)
                temp_self.chessboard = deepcopy(self.chessboard)
        
        else:

            for temp_x_y in hypothetical_moves_list:
                temp_self.move(retrieve_loc(temp_x_y))
                check = temp_self.chessboard.bki.check_for_check()
                if not check:
                    possible_moves.append(temp_x_y)
                temp_self = deepcopy(self)
                temp_self.chessboard = deepcopy(self.chessboard)
            

            for temp_x_y in hypothetical_capture_list:
                temp_self.capture(retrieve_loc(temp_x_y))
                check = temp_self.chessboard.bki.check_for_check()
                if not check:
                    possible_captures.append(temp_x_y)
                temp_self = deepcopy(self)
                temp_self.chessboard = deepcopy(self.chessboard)
        
        return possible_moves, possible_captures

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

    # can't castle under check and while attack between

    def castling(self):

        if self.color == "w" and self.castle and self.chessboard.wki.castle:
            emptyness =False
            minimum = min(self.x_y[1],self.chessboard.wki.x_y[1])
            spaces = abs(self.x_y[1]-self.chessboard.wki.x_y[1])-1
            count = 0

            # checking whether the spaces between the king and rook are empty

            for x in range(spaces):
                if self.chessboard.board[0][minimum + x+1].color == "X":
                    count+=1
            
            

            if count == spaces:
                emptyness = True
                
            if emptyness:
                
                if minimum == self.x_y[1]:
                    no_castle = False
                    for x in self.chessboard.black_piece_list:
                        attack_matrix = x.generate_attack_matrix()
                        print(attack_matrix[0][3]==1)
                        if attack_matrix[0][2]==1 or attack_matrix[0][3]==1 or attack_matrix[0][4]==1:
                            no_castle = True
                            break
                    if not no_castle:
                        move_maker(self.chessboard.wki,[0,2])
                        move_maker(self,[0,3])
                        self.castle = False
                        self.chessboard.wki.castle = False
                    else:
                        print("60 invalid move")

                else:
                    no_castle = False
                    for x in self.chessboard.black_piece_list:
                        attack_matrix = x.generate_attack_matrix()
                        if attack_matrix[0][6]==1 or attack_matrix[0][5]==1 or attack_matrix[0][4]==1:
                            no_castle = True
                            break
                    if not no_castle:
                        move_maker(self.chessboard.wki,[0,6])
                        move_maker(self,[0,5])
                        self.castle = False
                        self.chessboard.wki.castle = False
                    else:
                        print("61 invalid move")
            else:
                print("8 invalid move")

        
        elif self.color == "b" and self.castle and self.chessboard.bki.castle:
            emptyness = False
            minimum = min(self.x_y[1],self.chessboard.bki.x_y[1])
            spaces = abs(self.x_y[1]-self.chessboard.bki.x_y[1])-1
            count = 0

            # checking whether the spaces between the king and rook are empty

            for x in range(spaces):
                if self.chessboard.board[7][minimum + x+1].color == "X":
                    count+=1
            
            if count == spaces:
                emptyness = True
                
            if emptyness:
                if minimum == self.x_y[1]:
                    no_castle = False
                    for x in self.chessboard.white_piece_list:
                        attack_matrix = x.generate_attack_matrix()
                        if attack_matrix[7][2]==1 or attack_matrix[7][3]==1 or attack_matrix[7][4]==1:
                            no_castle = True
                            break
                    if not no_castle:
                        move_maker(self.chessboard.bki,[7,2])
                        move_maker(self,[7,3])
                        self.castle = False
                        self.chessboard.bki.castle = False
                    else:
                        print("62 invalid move")
                else:
                    no_castle = False
                    for x in self.chessboard.white_piece_list:
                        attack_matrix = x.generate_attack_matrix()
                        if attack_matrix[7][6]==1 or attack_matrix[7][5]==1 or attack_matrix[7][4]==1:
                            no_castle = True
                            break
                    if not no_castle:
                        move_maker(self.chessboard.wki,[7,6])
                        move_maker(self,[7,5])
                        self.castle = False
                        self.chessboard.bki.castle = False
                    else:
                        print("63 invalid move")
                
            else:
                print("9 invalid move")


        # needs to perform castle
        
    def move(self,final_location):
        castle = self.castle
        self.castle = False

        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="X":
            move_maker(self,final_x_y)
        else:
            print("10 invalid move")
            self.castle = castle
        # move to location
 
    def capture(self,final_location):
        castle = self.castle
        self.castle = False
        final_x_y = retrieve_x_y(final_location)

        if self.color == "b":

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="w":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("11 invalid move")
                self.castle = castle
        
        else:

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="b":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("12 invalid move")
                self.castle = castle

    def generate_attack_matrix(self):
        # needs to generate the places of possible attack
        attack_matrix = [[0 for x in range(8)] for x in range(8)]
        x= self.x_y[0]
        y= self.x_y[1]
        while x<7 :
            x+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break

        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 :
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while y<7 :
            y+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while y>0 :
            y-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        return attack_matrix

    def return_possible_moves(self):
        
        return piece_possible_moves(self)

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
        self.no_of_moves = 0

    # returns True if there is a check

    def check_for_check(self):
        check = False
        if self.color == "w":
            for x in self.chessboard.black_piece_list:
                attack_matrix = x.generate_attack_matrix()
                if attack_matrix[self.x_y[0]][self.x_y[1]]==1:
                    check = True
                    break
        if self.color == "b":
            for x in self.chessboard.white_piece_list:
                attack_matrix = x.generate_attack_matrix()
                if attack_matrix[self.x_y[0]][self.x_y[1]]==1:
                    check = True
                    break
        return check

    def move(self,final_location):
        castle = self.castle

        self.castle = False

        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="X":
            move_maker(self,final_x_y)
        else:
            print("13 invalid move")
            self.castle = castle
        # move to location
    
    def capture(self,final_location):
        castle = self.castle

        self.castle = False

        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if self.color == "b":

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="w":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("14 invalid move")
                self.castle = castle
        
        else:

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="b":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("15 invalid move")
                self.castle = castle

        # pretty much move

    def generate_attack_matrix(self):
        
        attack_matrix = [[0 for x in range(8)] for x in range(8)]
        x= self.x_y[0]
        y= self.x_y[1]
        if y!=0:
            try:
                attack_matrix[x][y-1]=1
            except:
                pass
        try:
            attack_matrix[x][y+1]=1
        except:
            pass
        if x!=0:
            if y!=0:
                try:     
                    attack_matrix[x-1][y-1]=1
                except:
                    pass
            try:
                attack_matrix[x-1][y]=1
            except:
                pass
            try:
                attack_matrix[x-1][y+1]=1
            except:
                pass
        if y!=0:
            try:
                attack_matrix[x+1][y-1]=1
            except:
                pass
        try:
            attack_matrix[x+1][y]=1
        except:
            pass
        try:
            attack_matrix[x+1][y+1]=1
        except:
            pass
        
        return attack_matrix
        
    def check_for_checkmate():
        if self.no_of_moves == 0:
            return True
    
    def return_possible_moves(self):
        
        return piece_possible_moves(self)

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
        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="X":
            move_maker(self,final_x_y)
        else:
            print("16 invalid move")
          
    def capture(self,final_location):

        final_x_y = retrieve_x_y(final_location)

        if self.color == "b":

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="w":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("17 invalid move")

        
        else:

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="b":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("18 invalid move")

    def generate_attack_matrix(self):
        attack_matrix = [[0 for x in range(8)] for x in range(8)]
        x= self.x_y[0]
        y= self.x_y[1]
        while x<7 :
            x+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break

        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 :
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while y<7 :
            y+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while y>0 :
            y-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x<7 and y<7:
            y+=1
            x+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 and y<7:
            y+=1
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x<7 and y>0:
            y-=1
            x+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 and y>0:
            y-=1
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break

        return attack_matrix

    def return_possible_moves(self):
        
        return piece_possible_moves(self)

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
        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="X":
            move_maker(self,final_x_y)
        else:
            print("19 invalid move")

    def capture(self,final_location):
        
        final_x_y = retrieve_x_y(final_location)

        if self.color == "b":

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="w":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("20 invalid move")

        
        else:

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="b":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("21 invalid move")

    def generate_attack_matrix(self):
        attack_matrix = [[0 for x in range(8)] for x in range(8)]
        x= self.x_y[0]
        y= self.x_y[1]
        print(x<7 and y<7)
        while x<7 and y<7:

            y+=1
            x+=1
            print(x,y,retrieve_loc((x,y)))
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 and y<7:
            y+=1
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x<7 and y>0:
            y-=1
            x+=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        x= self.x_y[0]
        y= self.x_y[1]
        while x>0 and y>0:
            y-=1
            x-=1
            attack_matrix[x][y]=1
            if self.chessboard.board[x][y].color!="X":
                break
        return attack_matrix

    def return_possible_moves(self):
        
        return piece_possible_moves(self)

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
        final_x_y = retrieve_x_y(final_location)

        attack_matrix = self.generate_attack_matrix()

        if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="X":
            move_maker(self,final_x_y)
        else:
            print("22 invalid move")
    
    def capture(self,final_location):
        final_x_y = retrieve_x_y(final_location)

        if self.color == "b":

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="w":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("23 invalid move")

        
        else:

            attack_matrix = self.generate_attack_matrix()

            if attack_matrix[final_x_y[0]][final_x_y[1]] == 1 and self.chessboard.board[final_x_y[0]][final_x_y[1]].color=="b":
                self.chessboard.remove_piece(self.chessboard.board[final_x_y[0]][final_x_y[1]])
                move_maker(self,final_x_y)
            else:
                print("24 invalid move")

    def generate_attack_matrix(self):
        attack_matrix = [[0 for x in range(8)] for x in range(8)]
        x= self.x_y[0]
        y= self.x_y[1]

        if y + 2 <= 7:
            if x + 1 <= 7:
                attack_matrix[x + 1][y + 2] = 1
            if x - 1 >= 0:
                attack_matrix[x - 1][y + 2] = 1
        if y - 2 >= 0:
            if x + 1 <= 7:
                attack_matrix[x + 1][y - 2] = 1
            if x - 1 >= 0:
                attack_matrix[x - 1][y - 2] = 1
        if x + 2 <= 7:
            if y + 1 <= 7:
                attack_matrix[x + 2][y + 1] = 1
            if y - 1 >= 0:
                attack_matrix[x + 2][y - 1] = 1
        if x - 2 >= 0:
            if y + 1 <= 7:
                attack_matrix[x - 2][y + 1] = 1
            if y - 1 >= 0:
                attack_matrix[x - 2][y - 1] = 1

        return attack_matrix

    def return_possible_moves(self):
        
        return piece_possible_moves(self)

    def update(self,chessboard):
        self.chessboard = chessboard

if __name__ == "__main__":
    a= chessboard()
    a.white_piece_list[0].castling()
    a.print_board()
    '''for x in a.dictionary.keys():
        print(x,":",a.dictionary[x][0].name)
    print(a.board[0][3].color,numpy.array(a.black_piece_list[-1].generate_attack_matrix()),a.black_piece_list[-1].name,a.black_piece_list[-1].loc,a.black_piece_list[-1].x_y)'''


    '''p = a.color_all_possible_moves("b")
    print(p[0])
    print(p[1])'''

    