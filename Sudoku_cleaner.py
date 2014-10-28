import csv
import math

def csv_to_list(puzzlefilename):#done
    puzzle = file_reader(puzzlefilename, puzzlelist = [])
    puzzle, dimension, valid_sudoku = cleaner_checker(puzzle)
    print('Your puzzle as a list is: ')
    print(puzzle)
    return puzzle, dimension, valid_sudoku

def file_reader(puzzlefilename, puzzlelist = []):#done
    with open(puzzlefilename, newline='') as f:
        reader = csv.reader(f)
        puzzlelist = list(reader)
    return puzzlelist


def cleaner_checker(listtocheck):#done
    dimension, valid_sudoku = length_counter(listtocheck)
    checkedlist, valid_sudoku = list_cleaner_checker(listtocheck,\
                                                     dimension, valid_sudoku)
    return checkedlist, dimension, valid_sudoku


def length_counter(listtocount, valid_sudoku = True):#done
    dimension = int(math.sqrt(len(listtocount)))
    for i in range(dimension**2):
        if len(listtocount[i]) != dimension**2:
            print('You have at least one row different in length from the'\
                  ' columns, so this cannot be a Sudoku puzzle.')
            valid_sudoku = False
    return dimension, valid_sudoku

def list_cleaner_checker(listtoclean, dimension, valid_sudoku):#done
    for i in range(dimension**2):
        for j in range(dimension**2):
            listtoclean[i][j] = int(listtoclean[i][j])
            if listtoclean[i][j] < 0:
                print('There is a value < 0 in your input file.')
                valid_sudoku = False
            elif listtoclean[i][j] > dimension**2:
                print('There is a value > ' + repr(dimension**2) +\
                      ' in your input file.')
                valid_sudoku = False
    return listtoclean, valid_sudoku
        
