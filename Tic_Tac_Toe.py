# display the board from the inputed cell list
def display(toe_str):
    print("-"*9)
    print("|{0:>2s}{1:>2s}{2:>2s} |".format(toe_str[0], 
                                            toe_str[1], toe_str[2]))
    print("|{0:>2s}{1:>2s}{2:>2s} |".format(toe_str[3], 
                                            toe_str[4], toe_str[5]))
    print("|{0:>2s}{1:>2s}{2:>2s} |".format(toe_str[6], 
                                            toe_str[7], toe_str[8]))
    print("-"*9)


# checks to see if there are 3 in a row
def checker(matrix, letter):
    letter_win = False

    # checking rows
    for x in range(0, 3):
        if matrix[x].count(letter) == 3:
            letter_win = True

    # checking columns
    column_count = 0
    for y in range (0, 3):
        for x in range (0, 3):
            if matrix[x][y] == letter:
                column_count += 1
        if column_count == 3:
            letter_win = True
        column_count = 0

    # checking diagonal
    diag_count = 0
    for i in range(0, 3):
        if matrix[i][i] == letter:
            diag_count += 1
    if diag_count == 3:
        letter_win = True
    diag_count = 0

    x = 0
    for y in range(2, -1, -1):
        if matrix[x][y] == letter:
            diag_count += 1
        x += 1
    if diag_count == 3:
        letter_win = True

    return letter_win


# is there a winner or was the data entered incorrectly
# this will print: X wins, O wins, Draw, or Impossible
def results(toe_str):
    finished = True
    x_win = False
    o_win = False

    # checking to see if the Xs and Os are balanced
    if (toe_str.count("X") - toe_str.count("O")) not in (-1, 0, 1):
        return "Impossible"

    # search for " " to see if the game is finished
    if toe_str.count(" ") > 0:
        finished = False

    # converting the string into a matrix
    toe_matrix = matrix_maker(toe_string)

    # sending the matrix to the checker for X
    x_win = checker(toe_matrix, "X")

    # sending the matrix to the checker for O
    o_win = checker(toe_matrix, "O")

    if x_win and o_win:
        return "Impossible"

    if not x_win and not o_win:
        if finished:
            return "Draw"
        else:
            return "no"

    if x_win:
        return "X wins"

    if o_win:
        return "O wins"


# converts the cell list into a 3 X 3 matrix
def matrix_maker(toe_str):
    toe_matrix = []
    str_pos = 0
    for x in range(3):
        toe_matrix.append([])
        for y in range(3):
            toe_matrix[x].append(toe_str[str_pos])
            str_pos += 1
    return toe_matrix

# gets the coordinates for the next X and removes any spaces
def get_coords():
    return input("Enter the coordinates: ").replace(" ", "")

# This ensures that the input is just numbers and 
# makes a list of integers from the input
def input_num_checker(coord_string):
    while not coord_string.isdecimal():
        print("You should enter numbers!")
        coord_string = get_coords()

    # convert to numbers, reduce by 1 to line up with 
    # the matrix, and make a list
    numbers = [(int(num) - 1) for num in coord_string]
    return numbers


# make sure that the numbers are in the range of 0 - 2
def in_range(coords):
    in_range_checker = False
    while in_range_checker == False:
        for i in range(2):
            if coords[i] > 2 or coords[i] < 0:
                print("Coordinates should be from 1 to 3!")
                coords = get_coords()
                coords = input_num_checker(coords)
            else:
                in_range_checker = True

    return coords


# this finds out which spaces are occupied
def occupied(coords, matrix, turn):
    is_occupied = False
    while is_occupied == False:
        if matrix[coords[0]][coords[1]] != " ":
            print("This cell is occupied! Choose another one!")
            coords = get_coords()
            coords = input_num_checker(coords)
            coords = in_range(coords)
        else:
            is_occupied = True

    # insert an "X" or "O" into the matix at the location
    # specified by the coordinates and return the changed matrix
    if turn % 2 == 0:
        matrix[coords[0]][coords[1]] = "O"
    else:
        matrix[coords[0]][coords[1]] = "X"
    return matrix

# **** Main ****

# starting with an empty board of 9 spaces
toe_string = "         "

# control the loop with the results function
is_over = "no"

# a counter to keep track of whose turn it is (X first)
turn = 1

# continue the game until there is 
# a winner or the game is a draw
while is_over == "no":

    # display the board
    display(toe_string)

    # getting the coordinates for the next move
    coords = input_num_checker(get_coords())

    # ensure that the coordinates are in range
    coords = in_range(coords)        

    # ensure that the cell is not occupied
    matrix = occupied(coords, matrix_maker(toe_string), turn)
    turn += 1

    # convert the matrix back to a list and get the results
    toe_string = [cell for row in matrix for cell in row]
    is_over = results(toe_string)

# displaying the final results
display(toe_string)
print(is_over)

