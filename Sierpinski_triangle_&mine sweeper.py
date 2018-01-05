"""
*Student Name: Raz Shenkman
*Student ID: 311130777
*Course Exercise Group: 01
*Exercise Name: ex7
"""

import argparse
import random
import turtle

# defining mysteryFunc
def mysteryFunc(a, n):
    """"
    The function prints the number a as a sum of the output
    numbers multiplied by the input n in power of the sum order
    (for example - if a is 10 and n is 2- the output will be 0-
    1-0-1 which means 0*(2^0) + 1*(2^1) + 0*(2^2) +1*(2^3),
    this function works for every a and n, except if n equals 1
    or 0 (because if n is equal to 1 it will never change the
    value of a, and if n equals to 0 then it will divide a by 0
    which is forbidden).

    The function gets the parameters a and n, first it checks
    if a is bigger than 0, if it is- it prints a % n (value of
    n never changes) and calls itself with the value (a / n, n)
    Keyword argument:
    a, n
    Return:
    if a> 0, the function calls itself after printing a % n by the
    parameters (a/n , n)
    """
    if a > 0:
        print a % n
        return mysteryFunc(a / n, n)

# defining class Sierpinski
class Sierpinski(object):

    def __init__(self):
        """"
        this function initializes the turtle and the window for the turtle
        to draw in
        Keyword argument:
        self(call it with 0 arguments)
        Return:
        none
        """
        self.window = turtle.Screen()
        self.sierpinski_turtle = turtle.Turtle()

    def draw_sierpinski(self, length, depth):
        """"
        this function draws the sierpinski triangle in a recursive way,
        the 'stop point' of the recursion is where the depth is 0, which prints
        3 triangles and takes the turtle to where we started.
        (by printing the length and turn 120 degrees after each print).
        when the depth is bigger than 0, it starts the recursive calling.
        the user calls the function again with the arguments the print the
        triangles in the left side of the big triangle,  then the turtle moves
        forward (right on the screen)and print the triangles in the right side
        of the big triangle. than the turtle moves up and backwards (up and left
        on the screen) and print triangles in the upper place of of the big
        triangle. so the triangle is fully printed now recursively
        Keyword argument:
        self(but we don't call the function with self), length, depth (user's
        input via arg parse which received and processed in main)
        Return:
        none
        """
        if depth == 0:
            for index in range(3):
                self.sierpinski_turtle.forward(length)
                self.sierpinski_turtle.left(120)
        else:
            # print the triangles in the left side
            self.draw_sierpinski(length/2, depth - 1)
            self.sierpinski_turtle.forward(length/2)
            # print the triangles in the right side
            self.draw_sierpinski(length/2, depth - 1)
            self.sierpinski_turtle.backward(length/2)
            self.sierpinski_turtle.left(60)
            self.sierpinski_turtle.forward(length/2)
            self.sierpinski_turtle.right(60)
            # print the triangles in the upper part
            self.draw_sierpinski(length/2, depth - 1)
            # return to the starting point
            self.sierpinski_turtle.left(60)
            self.sierpinski_turtle.backward(length/2)
            self.sierpinski_turtle.right(60)

    def finish_draw(self):
        """"
        this function closes the turtle print window after the print is done
        Keyword argument:
        self(call it with 0 arguments)
        Return:
        none
        """
        self.window.bye()

    def save_draw(self, length, depth):
        """"
        this function saves the window after the turtle finished working (it
        also hides the turtle)- it saves by using postscript on the windows
        which the finished triangle is print on
        Keyword argument:
        self(but we don't call the function with self), length, depth (user's
        input via arg parse which received and processed in main)
        Return:
        none
        """
        self.sierpinski_turtle.hideturtle()
        name_sav = ("sierpinski_%d_%d" % (length, depth)) + ".svg"
        ts = turtle.getscreen().getcanvas()
        ts.postscript(file=name_sav)

# defining class GameStatus
class GameStatus(object):
    """Enum of possible Game statuses."""
    __init__ = None
    NotStarted, InProgress, Win, Lose = range(4)

# defining class BoardCell
class BoardCell(object):
    """
    Represents a cell in the minesweeper board game and is current status in the
    game
    """
    def __init__(self):
        """
        Initializes a board cell with no neighboring mines and status is hidden
        .value is the number of neighbors or -1 if it has mine in it, and
        .status is if the cell is hidden 'H' or seen 'S'
        Args:
        None
        Returns:
        None (alters self)
        """
        self.value = 0
        self.status = 'H'

    def is_mine(self):
        """
        returns true if this cell contains a mine false otherwise, if it has a
        mine than it's value is -1
        Args:
        None
        Returns:
        true if this cell contains a mine false otherwise
        """
        if self.value is -1:
            return True
        else:
            return False

    def is_hidden(self):
        """
        returns true if this cell is hidden (it's status is -1)
        and false otherwise (it's status is 'S')
        Args:
        None
        Returns:
        true if this cell is hidden false otherwise
        """
        if self.status is 'H':
            return True
        else:
            return False

    def get_cell_value(self):
        """
        returns the number of adjacent mines (value of the cell)
        Args:
        None
        Returns:
        the number of adjacent mines in int or the charcter '*' if this cell
        is a mine
        """
        if self.value == -1:
            return '*'
        else:
            return self.value
        pass

    def uncover_cell(self):
        """
        uncovers this cell. when a cell is uncovered then is status is the value
        of the mines near it or * if the cell is a mine
        Args:
        None
        Returns:
        None (alters self)
        """
        if self.status == 'H':
            self.status = 'S'
        pass

    def update_cell_value(self, cellValue):
        """
        updates the value of the how many neighboring mines this cell has,
        if the cell's value isn't '*'
        this function takes the cell value from submission board and put's it
        in the correct cell in the original board.
        Args:
        numOfNearMine - the new number of the how many neighboring mines this
        cell has
        Returns:
        None (alters self)
        """
        if cellValue == '*':
            self.value = -1
        else:
            self.value = cellValue
        pass

    def add_one_to_cell_value(self):
        """
        adds one to the number of near mine, if the cell isn't a mine
        Args:
        None
        Returns:
        None (alters self)
        """
        if self.value != -1:
            self.value += 1
        pass


    def set_has_mine(self):
        """
        changes this cell to a cell with a mine in it (.value is -1)
        Args:
        None
        Returns:
        None (alters self)
        """
        self.value = -1


# defining class Board
class Board(object):
    """Represents a board of minesweeper game and its current progress."""

    def __init__(self, rows, columns):
        """Initializes an empty hidden board.

        The board will be in the specified dimensions, without mines in it,
        and all of its cells are in hidden state.

        Args:
        rows: the number of rows in the board
        columns: the number of columns in the board

        Returns:
        None (alters self)
        """
        self.numRows = rows
        self.numColumns = columns
        # creates board with row*col board cells
        self.board = [[BoardCell() for _ in range(columns)] for _ in range(rows)]

    def put_mines(self, mines, seed=None):
        """Randomly scatter the requested number of mines on the board.
        At the beggining, all cells on the board are hidden and with no mines
        at any of them. This method scatters the requested number of mines
        throughout the board randomly, only if the board is in the beginning
        state (as described here). A cell can host only one mine.
        This method not only scatters the mines on the board, but also updates
        the cells around it (so they will hold the right digit).

        Args:
        mines: the number of mines to scatter
        seed: the seed to give the random function. Default value None

        Returns:
        None (alters self)

        """

        listOfCellsIndex = [(numRow, numCol) for numRow in range(self.numRows)\
                            for numCol in range(self.numColumns)]
        # randomly choosing cells in the board to place mines in
        random.seed(seed)
        listOfMineCells = random.sample(listOfCellsIndex, mines)
        for cord in listOfMineCells:
            # set the cell in the board to a mine cell (by picking the same
            # cell from the random mines list)
            self.board[cord[0]][cord[1]].set_has_mine()
            for i in range(-1,2):
                for j in range(-1,2):
                    # if the cell isn't out of the board boundaries
                    if 0<=cord[0]+i < self.numRows and 0<=cord[1] + j < self.numColumns:
                        self.board[cord[0]+i][cord[1]+j].add_one_to_cell_value()

    def print_board(self):
        """prints the board according to the game format
        DO NOT CHANGE ANYTHING IN THIS FUNCTION!!!!!!!
        Args:
        None
        Returns:
        None
        """
        # creates the printing format
        printFormatString = "%-2s " * self.numColumns
        printFormatString += "%-2s"
        # prints the first line of the board which is the line containing the
        # indexes of the columns
        argList = [" "]
        argList.extend([str(i) for i in range(self.numColumns)])
        print printFormatString % tuple(argList)
        # goes over the board rows and prints each one
        for i in range(self.numRows):
            argList = [str(i)]
            for j in range(self.numColumns):
                if self.board[i][j].is_hidden():
                    argList.append("H")
                else:
                    argList.append(str(self.board[i][j].get_cell_value()))
            print printFormatString % tuple(argList)

    def load_board(self, lines):
        """Loads a board from a sequence of lines.

        This method is used to load a saved board from a sequence of strings
        (that usually represent lines). Each line represents a row in the table
        in the following format:
            XY XY XY ... XY
        Where X is one of the characters: 0-8, * and Y is one of letters: H, S.
        0-8 = number of adjusting mines (0 is an empty, mine-free cell)
        * = represents a mine in this cell
        H = this cell is hidden

        The lines can have multiple whitespace of any kind before and after the
        lines of cells, but between each XY pair there is exactly one space.
        Empty or whitespace-only lines are possible between valid lines, or
        after/before them. It is safe to assume that the values are correct
        (the number represents the number of mines around a given cell) and the
        number of mines is also legal.
        Note that this method doesn't get the first two rows of the file (the
        dimensions) on purpose - they are handled in __init__.

        Args:
        lines: a sequence (list or tuple) of lines with the above restrictions

        Returns:
           None (alters self)
        """
        # creates a new list
        newLines = []
        # run over the lines in the submission board and copying them without
        # the chars 'H' and 'space' to the newLines new list
        for line in lines:
            newLines.extend((line.replace(' ','').replace('H','')))

        # run over the lines in the board and updating it's cells value to have
        # the correct value by the value of the cells in their spot in
        # submission board
        for cellLine in self.board:
            for spesCell in cellLine:
                spesCell.update_cell_value(newLines[0])
                # removes the copied cell value from the list of cells from
                # submission board
                newLines.remove(newLines[0])

        pass

    def get_value(self, row, column):
        """
        Returns the value of the cell at the given indices.
        The return value is a string of one character, out of 0-8 + '*'.

        Args:
        row: row index (integer)
        column: column index (integer)

        Returns:
        If the cell is empty and has no mines around it, return '0'.
        If it has X mines around it (and none in it), return 'X' (digit
        character between 1-8).
        If it has a mine in it return '*'.
        """
        # get the cell's value from the board and check it's value
        cellVal = self.board[row][column].get_cell_value()
        if cellVal == 0:
            return 0
        elif cellVal > 0:
            return cellVal
        else:
            return '*'
        pass

    def is_hidden(self, row, column):
        """
        Returns if the given cell is in hidden or uncovered state.

        Args:
        row: row index (integer)
        column: column index (integer)

        Returns:
        'H' if the cell is hidden, or 'S' if it's uncovered (can be seen).
        """
        # check the cell's status from the board
        cellStat = self.board[row][column].is_hidden()
        if cellStat:
            return 'H'
        else:
            return 'S'
        pass

    def uncover(self, row, column):
        """
        Changes the status of a cell from hidden to seen. from 'H' to 'S'

        Args:
        row: row index (integer)
        column: column index (integer)

        Returns:
        None (alters self)
        """
        cellStat = self.board[row][column].is_hidden()
        if cellStat:
            self.board[row][column].status = 'S'
        pass


# defining class Game
class Game(object):
    """Handles a game of minesweeper by supplying UI to Board object."""

    def __init__(self, board):
        """
        Initializes a Game object with the given Board object.
        The Board object can be a board in any given status or stage.

        Args:
        board: a Board object to continue (or start) playing.
        Returns:
        None (alters self)
        """
        self.gameBoard = board
        pass

    def get_status(self):
        """
        Returns the current status of the game.
        The current status of the game is as followed:
        NotStarted: if all cells are hidden.
        InProgress: if some cells are hidden and some are uncovered, and
            no cell with a mine is uncovered.
        Lose: a cell with mine is uncovered.
        Win: All non-mine cells are uncovered, and all mine cells are
        covered.
        Args:
        self
        Returns:
        one of GameStatus values (doesn't alters self)
        """
        indicator1 = 0
        indicator2 = 0
        winIndicator = 0
        row = self.gameBoard.numRows
        column = self.gameBoard.numColumns
        # go through the board cells and check their status
        for i in range(row):
            for j in range(column):
                # if cell is visible than the game NotStarted
                if self.gameBoard.is_hidden(i,j) == 'S':
                    indicator1 = 1
                # if cell has a mine and it's hidden- InProgress, else- Lose
                if self.gameBoard.get_value(i,j) == '*':
                    if self.gameBoard.is_hidden(i, j) == 'H':
                        indicator2 = 1
                    else:
                        return GameStatus.Lose
                # if all the cells without mines are visible- Win
                if self.gameBoard.get_value(i,j) != '*' and \
                    self.gameBoard.is_hidden(i,j) =='H':
                        winIndicator = 1
        # if the cells without mines are visible
        if winIndicator == 0:
            return GameStatus.Win
        # if all cells are with status 'H'
        if indicator1 == 0:
            return GameStatus.NotStarted
        # if there are cells hidden with mines (check the condition if all cells
        # are hidden before- with indicator1
        if indicator2 == 1:
            return GameStatus.InProgress
        pass

    def make_move(self, row, column):
        """
        Makes a move by uncovering the given cell and unrippling it's area.
        this function works recursevely on the first cell inputted to uncover,
        if it's value is '*' then it will just uncover the cell and won't start
        the recursion.
        if it's value is 0 than it runs on the 8 cells thats around it, checking
        their neighbors value and continue uncovering cells until it gets to a
        cell that is already uncovered, has a neighbor mine or a cell with a
        mine in it.
        The move flow is as following:
        1. Uncover the cell
        2. If the cell is a mine - return
        3. if the cell is not a mine, ripple (if value = 0) and uncover all
            adjacent cells, and recursively on this cells if needed (if they are
            empty cells)
        Args:
            row: row index (integer)
            column: column index (integer)
        Returns:
            the cell's value.
        """


        self.gameBoard.uncover(row,column)
        if self.gameBoard.get_value(row,column) == '*':
            return
        # check if it's value is '0' because the str value from submission board
        if (self.gameBoard.get_value(row,column) == '0') or \
            (self.gameBoard.get_value(row, column) == 0):
            for i in range(-1,2):
                for j in range(-1,2):
                    # the if the neighbor cells are in the board boundaries
                    if (0 <= row + i < self.gameBoard.numRows) and \
                     (0 <= column + j < self.gameBoard.numColumns and\
                         self.gameBoard.is_hidden(row+i,column+j) == 'H'):
                        # calling the function recursively on the neighbor cells
                        self.make_move(row+i,column+j)
        return self.gameBoard.get_value

    def run(self):
        """
        Runs the game loop.
        At each turn, prints the following:
        current state of the board
        game status
        available actions
        And then wait for input and act accordingly.
        More details are in the project's description.

        use get_status function to check the board status.

        Returns:
            None
        """

        self.gameBoard.print_board()
        # if the game hasn't started yet
        if self.get_status() == GameStatus.NotStarted:
            print("Game status: NotStarted")
            print("Available actions: (1) Exit | (2) Move")
            print("Enter selection: ")
            ch = raw_input()
            if ch == '1':
                print("Goodbye :)")
                exit()
            if ch == '2':
                print("Enter row then column (space separated):")
                row, column = raw_input().split(' ')
                if int(row) > self.gameBoard.numRows or int(
                        column) > self.gameBoard.numColumns:
                    print("Illegal move values")
                    self.run()
                # casting the inputted rows and columns to int
                if self.gameBoard.is_hidden(int(row), int(column)) == 'S':
                    print("Illegal move values")
                    self.run()
                self.make_move(int(row), int(column))
                self.run()
            else:
                print("Illegal choice")
                self.run()
        # if the user has won the game
        if self.get_status() == GameStatus.Win:
            print("Game status: Win")
            print("Available actions: (1) Exit")
            print("Enter selection: ")
            ch = raw_input()
            if ch == '1':
                print("Goodbye :)")
                exit()
            else:
                print("Illegal choice")
                self.run()
        # if the user has lost the game
        if self.get_status() == GameStatus.Lose:
            print("Game status: Lose")
            print("Available actions: (1) Exit")
            print("Enter selection: ")
            ch = raw_input()
            if ch == '1':
                print("Goodbye :)")
                exit()
            else:
                print("Illegal choice")
                self.run()
        # if the game is in progress
        if self.get_status() == GameStatus.InProgress:
            print("Game status: InProgress")
            print("Available actions: (1) Exit | (2) Move")
            print("Enter selection: ")
            ch = raw_input()
            if ch == '1':
                print("Goodbye :)")
                exit()
            if ch == '2':
                print("Enter row then column (space separated):")
                row,column = raw_input().split(" ")
                if int(row) > self.gameBoard.numRows or int(
                        column) > self.gameBoard.numColumns:
                    print("Illegal move values")
                    self.run()
                    # casting the inputted rows and columns to int
                if self.gameBoard.is_hidden(int(row), int(column)) == 'S':
                    print("Illegal move values")
                    self.run()
                self.make_move(int(row), int(column))
                self.run()
            else:
                print("Illegal choice")
                self.run()

        pass


def main():
    """
    Starts the game by parsing the arguments and initializing.
    Act according to the exercise explanation

    Regarding mine sweeper:
    If an input file argument was given, the file is loaded (even if other
    legal command line argument were given).

    If input file wasn't given, create a board with the rows/columns/mines

    In case both an input file was given and other parameters, ignore the
    others and use only the input file.
    For example, in case we get "-i sample -r 2 -c 2" just use
    the input file and ignore the rest (even if there are missing parameters).

    Returns:
    None

    """

    # declaring parser to be of arg parse type
    parser = argparse.ArgumentParser()
    # Required argument to choose which mission to operate
    parser.add_argument('-p', type=int,  help='choose_task')
    # Optional arguments
    parser.add_argument('-a', type=int, help='for mission 1')
    parser.add_argument('-n', type=int,  help='for mission 1')
    parser.add_argument('-d', type=int, help='for mission 2')
    parser.add_argument('-l', type=int, help='for mission 2')
    parser.add_argument('-r', type=int, help='for mission 3')
    parser.add_argument('-c', type=int, help='for mission 3')
    parser.add_argument('-m', type=int, help='for mission 3')
    parser.add_argument('-i', type=str, help='for mission 3')
    parser.add_argument('-s', type=float, help='for mission 3')
    args = parser.parse_args()
    # start mysteryFunc
    if args.p == 1:
        mysteryFunc(args.a, args.n)
    # start Sierpinski
    if args.p == 2:
        triangle = Sierpinski()
        triangle.draw_sierpinski(args.l, args.d)
        triangle.save_draw(args.l, args.d)
        triangle.finish_draw()
    # start mine sweeper
    if args.p == 3:
        if args.i:
            # open the file using read and write permissions
            subBoard = open(args.i, 'r+')
            # strip the line from spaces
            lines = [line.strip() for line in subBoard if line.strip()\
                .replace('  ', ' ')]
            args.r = int(lines[0])
            args.c = int(lines[1])
            # remove the lines of rows and columns
            lines.remove(lines[0])
            lines.remove(lines[0])
            # check if the rows and columns are in the correct restrictions
            if args.r >= 1 and args.r <= 20 and args.c >= 2 and args.c <= 50:
                # create new board to get the values from submitted board
                board = Board(args.r, args.c)
                board.load_board(lines)
                # run the game using the copied submitted board
                Game(board).run()
            else:
                print("Illegal board")
                exit()
        # check if the rows, columns and mines  are in the correct restrictions
        elif args.r >= 1 and args.r <= 20 and args.c >= 2 and args.c <= 50\
             and 0 <= args.m < (args.r*args.c):
            board = Board(args.r, args.c)
            board.put_mines(args.m,args.s)
            # run the game using the new board
            Game(board).run()
        else:
            print("Illegal board")
            exit()
    pass

if __name__ == '__main__':
    main()


