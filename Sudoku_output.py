import csv

def output_maker(solution, puzzlefilename, dimension):#done
    print('Your solution as a list is: ')
    print(solution)
    solutionfilename = filenamemaker(puzzlefilename)
    solutionfilewriter(solution, solutionfilename, dimension)
    
def filenamemaker(puzzlefilename):#done
    solutionfilename = puzzlefilename[:(len(puzzlefilename)-4)]\
                       + '_solution.csv'
    print('The solution is in ' + solutionfilename + '.')
    return solutionfilename

def solutionfilewriter(solution, solutionfilename, dimension):#done
    with open(solutionfilename, 'w', newline='') as f:
        solutionwriter = csv.writer(f, delimiter=',')
        for i in range(dimension**2):
            solutionwriter.writerow(solution[i])
