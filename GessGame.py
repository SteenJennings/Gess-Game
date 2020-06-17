# Author: Steinar Jennings
# Date: 6/4/2020
# Description: This program will execute a game called "Gess" that is a mix of GO and Chess, thus the name
# the players will make legal moves on the board trying to stay within the bounds while keeping a "hollow"
# square consisting of their colors. the first player to lose all of their "hollow squares" loses. Pieces are taken
# by 3x3 pieces stepping on them.


class GessGame:
    """
    A class that contains the methods and data members that make up the Gess game.The make_move method is the primary
    method in the class.It calls on other helper methods to receive input from the user and validate moves, which
    it does using other methods throughout the class.The game board is initialized to a standard starting position
    where the black color will move first.The boundaries of the board are not representative of the entire playing
    area, there are restrictions to where the “footprints” or 3x3 pieces can move.
    """

    def __init__(self):
        """initializes the starting board for and sets it to unfinished, and tracks."""
        self._board = (
            [["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
             ["_", "_", "B", "_", "B", "_", "B", "B", "B", "B", "B", "B", "B", "B", "_", "B", "_", "B", "_", "_", "2"],
             ["_", "B", "B", "B", "_", "B", "_", "B", "B", "B", "B", "_", "B", "_", "B", "_", "B", "B", "B", "_", "3"],
             ["_", "_", "B", "_", "B", "_", "B", "B", "B", "B", "B", "B", "B", "B", "_", "B", "_", "B", "_", "_", "4"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "5"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "6"],
             ["_", "_", "B", "_", "_", "B", "_", "_", "B", "_", "_", "B", "_", "_", "B", "_", "_", "B", "_", "_", "7"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "8"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "9"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "10"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "11"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "12"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "13"],
             ["_", "_", "W", "_", "_", "W", "_", "_", "W", "_", "_", "W", "_", "_", "W", "_", "_", "W", "_", "_", "14"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "15"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "16"],
             ["_", "_", "W", "_", "W", "_", "W", "W", "W", "W", "W", "W", "W", "W", "_", "W", "_", "W", "_", "_", "17"],
             ["_", "W", "W", "W", "_", "W", "_", "W", "W", "W", "W", "_", "W", "_", "W", "_", "W", "W", "W", "_", "18"],
             ["_", "_", "W", "_", "W", "_", "W", "W", "W", "W", "W", "W", "W", "W", "_", "W", "_", "W", "_", "_", "19"],
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "20"],
             ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]])
        self._game_state = "UNFINISHED"
        self._current_turn = "B"

    def get_game_state(self):
        """returns the current state "UNFINISHED" or the color of the winner if there is one"""
        return self._game_state

    def resign_game(self):
        """updates the game state to set the winner to be the opponents turn
        for example, if it is Blacks turn, white is set to the winner"""
        if self._current_turn == "B":
            self._game_state = "WHITE_WON"
        else:
            self._current_turn = "BLACK_WON"

    def update_turn(self):
        """this will be called after a valid move, non-winning move, to track whose turn it now is
        this is only updated at the end, because current turn is important for making the other methods
        dynamic to whichever color is making a move"""
        if self._current_turn == "B":
            self._current_turn = "W"
        else:
            self._current_turn = "B"

    def str_to_location(self, node_str):
        """converts to string to actionable coordinates in a list. For example it will convert c13
        to a list [2,12], by finding the index on the grid that those points refer to"""
        # we are subtracting one from the first half (row) , since the value will need to be converted to index form
        translated_columns = "abcdefghijklmnopqrst"
        coordinates = [(int(node_str[1:]) - 1), (int(translated_columns.index(node_str[0])))]
        return coordinates

    def get_direction(self, current_coord, end_coord):
        """this will evaluate which direction the proposed move is in, from our starting piece"""
        a = current_coord[0]
        b = current_coord[1]
        c = end_coord[0]
        d = end_coord[1]
        if c > a and d > b and (abs(c - a) == abs(d - b)):  # checks for valid diagonal move
            return "SE"
        elif c > a and d == b:
            return "S"
        elif c > a and d < b and (abs(c - a) == abs(d - b)):
            return "SW"
        elif c == a and d > b:
            return "E"
        elif c == a and d < b:
            return "W"
        elif c < a and d > b and (abs(c - a) == abs(d - b)):
            return "NE"
        elif c < a and d == b:
            return "N"
        elif c < a and d < b and (abs(c - a) == abs(d - b)):
            return "NW"

    def move_possible(self, user, row, column, direction):
        """checks to see if these is a stone in the direction that we identified above, relative
        to the center node."""
        if ((self._board[row - 1][column + 1] == user and direction == "NE") or
                (self._board[row - 1][column - 1] == user and direction == "NW") or
                (self._board[row][column + 1] == user and direction == "E") or
                (self._board[row + 1][column] == user and direction == "S") or
                (self._board[row][column - 1] == user and direction == "W") or
                (self._board[row - 1][column] == user and direction == "N") or
                (self._board[row + 1][column + 1] == user and direction == "SE") or
                (self._board[row + 1][column - 1] == user and direction == "SW")):
            return True
        else:
            return False    #if there is no stone, the move is impossible therefore we will need to return false.

    def check_board(self, board):
        """checks the board and evaluates using the "current_turn" data memeber to see if they still have a valid
        ring left"""
        user = self._current_turn
        count = 0
        for r in range(1, 19):  # checking from rows 2-19 (because of indexing)
            for c in range(1, 19):  # checking from columns 2-19 or b-s (because of indexing)
                if (board[r][c] == "_" and board[r - 1][c + 1] == user and
                        board[r - 1][c - 1] == user and board[r][c + 1] == user and
                        board[r + 1][c] == user and board[r][c - 1] == user and
                        board[r - 1][c] == user and board[r + 1][c + 1] == user and
                        board[r + 1][c - 1] == user):
                    count += 1
        if count > 0:
            return True
        else:
            return False

    def print_board(self):
        """method that prints the board one row at a time, used for visualizing the game"""
        for row in self._board:
            print(row)

    def zero_print(self, row, column):
        """this method clears the current footprint so we can move"""
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:        #clears every index (0,0) is the center node, (-1,-1) is the North
                self.temp_board[row + i][column + j] = "_"

    def make_move(self, start_node, end_node):
        """locates the coordinates of the start node and determines if it is a valid start node,
        and then evaluates the validity of the end node by traversing the board one step at a time
        to see if we are going to hit any nodes along the way, if we are able to legally execute the coordinates
        we will update the board and check to see if the game has been won. If not, we will update whose
        turn it is and continue playing the game. This code is explained in much greater detail with the relevant
        comment blocks throughout the code that explain what each section of the method does."""

        if self._game_state != "UNFINISHED":  # if the game has already been won
            return False

        # checks which direction the proposed move is in and stores that value as the "path" i.e. "SW"
        current_coord = self.str_to_location(start_node)
        end_coord = self.str_to_location(end_node)

        # checks if the target location is a valid destination (needs to check for all edges)
        if end_coord[0] > 18 or end_coord[1] > 18 or end_coord[0] < 1 or end_coord[1] < 1:
            return False

        # checks if the target location is a valid destination (needs to check for all edges)
        if current_coord[0] > 18 or current_coord[1] > 18 or current_coord[0] < 1 or current_coord[1] < 1:
            return False

        path = self.get_direction(current_coord, end_coord)

        # checks if the direction is movable from current node, see the docstring above
        user = self._current_turn
        valid_move = self.move_possible(user, current_coord[0], current_coord[1], path)
        if valid_move == False:
            return False  # the end_coord is unreachable

        row = current_coord[0]
        column = current_coord[1]
        # checks to make sure that our starting coordinate is only surrounded by empty spots or same colored spots
        if not ((self._board[row - 1][column + 1] == user or self._board[row - 1][column + 1] == "_") and
                (self._board[row - 1][column - 1] == user or self._board[row - 1][column - 1] == "_") and
                (self._board[row][column + 1] == user or self._board[row][column + 1] == "_") and
                (self._board[row + 1][column] == user or self._board[row + 1][column] == "_") and
                (self._board[row - 1][column] == user or self._board[row - 1][column] == "_") and
                (self._board[row + 1][column + 1] == user or self._board[row + 1][column + 1] == "_") and
                (self._board[row + 1][column - 1] == user or self._board[row + 1][column - 1] == "_")):
            return False

        # calculates how many "steps" we need to take to complete the move
        spaces_moved = max(abs(end_coord[0] - row), abs(end_coord[1] - column))
        # this will not allow us to check for validity of moves that are more than 3 steps
        if spaces_moved > 3 and self._board[row][column] != user:
            return False

        # we are creating a temporary board to test out the "path" that our footprint will move through, checking
        # for obstructions along the way. This section of code will also need the ability to check if
        # any part of the footprint will land "off" the board, if so, those pieces will need to be removed
        self.temp_board = []
        for i in self._board:
            self.temp_board.append(list(i))

        coords_dict = {"SE": [1, 1], "E": [0, 1], "NE": [-1, 1], "S": [1, 0], "N": [-1, 0], "SW": [1, -1], "W": [0, -1],
                       "NW": [-1, -1]}

        temp = 0 #used to track where we currently are
        i = 1 #used to track where we are trying to go next
        while i < spaces_moved:
            self.zero_print(row + temp * coords_dict[path][0], column + temp * coords_dict[path][1])
            temp += 1
            pos = [row + i * coords_dict[path][0], column + i * coords_dict[path][1]]
            for idx in [-1, 0, 1]:
                for idx2 in [-1, 0, 1]:
                    if self.temp_board[pos[0] + idx][pos[1] + idx2] != "_": #if its not empty, then we are obstructed
                        #print("Path is obstructed!")
                        return False
                    else:
                        continue
            i += 1

        #this section of code moves the end footprint to the ending destination. After checking for
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                self.temp_board[end_coord[0] + i][end_coord[1] + j] = self._board[current_coord[0] + i][current_coord[1] + j]

        #after moving the footprint to the end on the temp board, we check to make sure we didn't break any rings
        if self.check_board(self.temp_board) != True:
            return False

        temp_footprint = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]   #stores the piece we want to move

        #fills the temp footprint
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                temp_footprint[1 + i][1 + j] = self._board[row + i][column + j]
                self._board[row + i][column + j] = "_"

        #"Pastes" the temp footprint in the
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                self._board[end_coord[0] + i][end_coord[1] + j] = temp_footprint[1 + i][1 + j]

        # clears the pieces on the edges of the board, out of playing range.
        for i in range(20):
            self._board[0][i] = "_"
            self._board[19][i] = "_"
            self._board[i][0] = "_"
            self._board[i][19] = "_"

        # this section evaluates whether or not the opponent (after updating the turn) has a valid square left
        # the turn needs to be updated regardless, before anyone makes another move.
        winner_check = self._current_turn
        self.update_turn()
        if self.check_board(self._board) == False and winner_check == "B":
            self._game_state = "BLACK_WON"
            return True
        elif self.check_board(self._board) == False and winner_check == "W":
            self._game_state = "WHITE_WON"
            return True
        else:
            return True


# game = GessGame()
# print(game.make_move('m3', 'm6'))
# print(game.make_move('e14', 'g14'))
# print(game.get_game_state())
# game.resign_game()
# print(game.get_game_state())

# game = GessGame()
# game.print_board()
# print(game.make_move('r3', 'r4'))
# print(game.make_move('i18', 'i15'))
# game.print_board()
# print(game.make_move('r4', 'r3'))
# print(game.make_move('i15', 'i8'))
# print(game.make_move('r3', 'r4'))
# print(game.make_move('i8', 'k6'))
# print(game.make_move('r4', 'r3'))
# print(game.make_move('k6', 'k5'))
# print(game.get_game_state())

