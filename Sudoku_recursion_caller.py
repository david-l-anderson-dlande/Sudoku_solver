import Sudoku_recursion


def solver_master(puzzle, dimension):
    puzzle = solverloops(puzzle, dimension)
    squares_caller = squares_builder(puzzle, dimension)
    values = dict_builder(puzzle, dimension, squares_caller)
    answer_dict = Sudoku_recursion.solve(values, squares_caller, dimension)
    puzzle_solution = dict_to_matrix(answer_dict, squares_caller, dimension)
    return puzzle_solution



def squares_builder(puzzle, dimension):
    squares_caller = []
    for i in range(dimension**2):
        squares_caller.append([0]*((dimension**2)))
    for i in range(dimension**2):
        for j in range(dimension**2):
            squares_caller[i][j] = repr(i)+'_'+repr(j)
    return squares_caller

def dict_builder(puzzle, dimension, squares_caller):
    values={}
    for i in range(dimension**2):
        for j in range(dimension**2):
            if puzzle[i][j] == int(0):
                possible_elements = element_solver(puzzle, i, j, dimension)
                temp_number_string = string_converter(possible_elements)
                values[squares_caller[i][j]]=temp_number_string
            else:
                values[squares_caller[i][j]]=repr(puzzle[i][j])
    return values
    

def element_solver(puzzle, row, column, dimension):
    restricted_elements = restriction_builder(puzzle, row, column, dimension)
    element_list = elementlists_compare(restricted_elements, dimension)
    return element_list

def restriction_builder(puzzle, row, column, dimension):
    current_row, current_column, current_block =\
                 build_lists(puzzle, row, column, dimension)
    current_group = lists_reduce(current_row, current_column,\
                                 current_block, dimension)
    return current_group

def build_lists(puzzle, row, column, dimension):
    row_list = row_counter(puzzle, row, dimension)
    column_list = column_counter(puzzle, column, dimension)
    block_list = block_counter(puzzle, row, column, dimension)
    return row_list, column_list, block_list

def row_counter(puzzle, row, dimension):
    listforrow = []
    for i in range(dimension**2):
        listforrow.append(puzzle[row][i])
    return listforrow

def column_counter(puzzle, column, dimension):
    listforcolumn = []
    for i in range(dimension**2):
        listforcolumn.append(puzzle[i][column])
    return listforcolumn


def block_counter(puzzle, row, column, dimension):
    listforblock = []
    rowstart = dimension * int(row/dimension)
    columnstart = dimension * int(column/dimension)
    for i in range(rowstart, rowstart+dimension):
        for j in range(columnstart, columnstart+dimension):
            listforblock.append(puzzle[i][j])
    return listforblock


def lists_reduce(current_row, current_column, current_block, dimension):
    element_restrictions = []
    used_list = []
    used_list.extend(current_row)
    used_list.extend(current_column)
    used_list.extend(current_block)
    for i in range(dimension**2):
        if used_list.count(i+1) > 0:
            element_restrictions.append(i+1)
    return element_restrictions

def elementlists_compare(restricted, dimension):
    elements_left = list(range(dimension**2+1))
    elements_left.remove(0)
    for elem in restricted:
        elements_left.remove(elem)
    return elements_left


def string_converter(possible_elements):
    temp_string = ''
    for element in possible_elements:
        temp_string = temp_string+repr(element)
    return temp_string


def dict_to_matrix(answer_dict, squares_caller, dimension):
    if answer_dict == False:
        return 'Not a valid Sudoku.'
    else:
        tempmatrix = []
        for i in range(dimension**2):
            tempmatrix.append([0]*((dimension**2)))
        for i in range(dimension**2):
            for j in range(dimension**2):
                tempmatrix[i][j] = int(answer_dict[squares_caller[i][j]])
        return tempmatrix


def solverloops(puzzle, dimension):
    counter = 0
    while (counter < dimension**2):
        puzzle = element_iteration(puzzle, dimension)
        counter = counter + 1
    return puzzle


def element_iteration(puzzle, dimension):
    for i in range(dimension**2):
        for j in range(dimension**2):
            if puzzle[i][j] == 0:
                puzzle[i][j] = element_solver_loops(puzzle, i, j, dimension)
    return puzzle

def element_solver_loops(puzzle, row, column, dimension):
    restricted_elements = restriction_builder(puzzle, row, column, dimension)
    element = element_finder(restricted_elements, dimension)
    return element


def element_finder(elem_restrict, dimension):
    element_possible = elementlists_compare(elem_restrict, dimension)
    if len(element_possible) == 1:
        element = element_possible[0]
    else:
        element = 0
    return element


