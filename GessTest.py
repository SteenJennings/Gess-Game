from GessGame import GessGame

def test1(game):
    #tests for winning by breaking other's ring
    print(game.make_move('r3', 'r4'))
    print(game.make_move('i18', 'i15'))
    print(game.make_move('r4', 'r3'))
    print(game.make_move('i15', 'i8'))
    print(game.make_move('r3', 'r4'))
    print(game.make_move('i8', 'k6'))
    print(game.make_move('r4', 'r3'))
    print(game.make_move('k6', 'k5'))
    print(game.get_game_state())

def test2(game): #False
    #move off the board, from legal starting point
    print(game.make_move('c3', 'a3'))

def test3(game): #False
    #move legally on the board, from illegal starting point
    print(game.make_move('a3', 'b3'))

def test4(game): #True
    #checks to make sure we are "burning" the edge pieces
    print(game.make_move('c3', 'b3'))
    #game.print_board()

def test5(game): #False
    #move off the board, from legal starting point
    print(game.make_move('n3', 'n6'))
    #game.print_board()

def test6(game): #True
    #trying at least three variants of "odd" moves with one direction. Test for every direction.
    print("this is test 6")
    print(game.make_move('i4', 'i3')) #north
    print(game.make_move('i18', 'h18')) #west
    print(game.make_move("s4", "r3")) #northwest
    print(game.make_move('r17', 'q18')) #southwest
    print(game.make_move('c3', 'c4')) #south
    print(game.make_move('c18', 'd18')) #east
    print(game.make_move('f3', 'g4')) #southeast
    print(game.make_move('h18', 'j16')) #northeast

def test7(game):
    #handles a check for unlimited moves
    print(game.make_move('s7', 'p7'))
    print(game.make_move('s14', 'p14')) #west
    print(game.make_move('r3', 'r16'))

def test8(game):
    #readme test case
    print(game.make_move('p3', 'p6'))
    print(game.make_move('e14', 'g14'))
    print(game.resign_game())
    print(game.get_game_state())

def test9(game):
    #check to make sure footprint is made up of like pieces
    print(game.make_move('s7', 'p7'))
    print(game.make_move('s14', 'p14')) #west
    print(game.make_move('r3', 'r16'))
    print(game.make_move('q17', 'p17'))


game = GessGame()
game1 = GessGame()
game2 = GessGame()
game3 = GessGame()
game4 = GessGame()
game5 = GessGame()
game6 = GessGame()
game7 = GessGame()
game8 = GessGame()
game9 = GessGame()


test1(game)  #tests to see if the game can be won properly
test2(game1) #move off the board, from legal starting point
test3(game2) #move legally on the board, from illegal starting point
test4(game3) #checks to make sure we are "burning" the edge pieces
test5(game4) #blocks the player from making a suicidal move
test6(game5) #trying at least three variants of "odd" moves with one direction. Test for every direction.
test7(game6) #handles the case where we are trying to move without unlimited moves
test8(game7) #handles the specified cases in the readme
test9(game8) #trying to move a piece whose footprint conatins other colors

# The Edge Cases:Illegal move off the board. (Test)
# Move from illegal starting position (Test)
# "burning" the edge pieces. (Test)
# Trying to make a move that "kills the player", breaking my own ring (Test)
# Trying a move that moves our shield (Test)Winning moves, does the game state update. (Test)
# moving only one space. (Test)making a move in each direction. (Test)
# all the rules in the readme (Test) - Make a list
# trying to move a piece whose footprint conatins other colors
