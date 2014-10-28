#Sudoku Solver
#by David L. Anderson


import Sudoku_fileopener
import Sudoku_cleaner
import Sudoku_recursion_caller
import Sudoku_output


def sudokusolver(puzzlefilename = 'puttherealfilenamestringhere.csv'):
    puzzlefilename = Sudoku_fileopener.get_file_name(puzzlefilename)
    puzzle, dimension, valid_sudoku = Sudoku_cleaner.csv_to_list(puzzlefilename)
    if valid_sudoku == True:
        puzzle = Sudoku_recursion_caller.solver_master(puzzle, dimension)
        Sudoku_output.output_maker(puzzle, puzzlefilename, dimension)

if __name__ == "__main__":
    import sys
    sudokusolver()
 
