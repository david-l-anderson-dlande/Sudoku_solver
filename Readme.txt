The main file is Sudokusolver.py. Just put it in the directory with the .csv
representations of your problems, and run it. The other files simply need to
be somewhere in your Python path.

You could also import the function sudokusolver and then use it directly with
sudokusolver('filename.csv')

I think most of what the other files do is fairly evident from their names.
the _recursion_caller also goes through a few loops of a naive algorithm to 
give the recursion algorithm a bit less work.

Note that I have built this for any general n^2 x n^2 Sudoku; however, if you
have a .csv of Sudoku-zilla handy, I make no guarantees of results.