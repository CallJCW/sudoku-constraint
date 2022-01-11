import argparse
from constraint import *

def solve(puzzle):

  problem = Problem()
  domain = range(1,10)
  cols = range(9)
  rows = range(9)

  grid = []

  for row in rows: #Create all 81 variables and add uniqueness constraint for each row
      grid.append([])
      for column in cols:    
          grid[row].append(str(row) +','+ str(column))
      problem.addVariables(grid[row], domain)
      problem.addConstraint(AllDifferentConstraint(), grid[row])

  collist = []
  for column in cols: #Add uniqueness constraint for each column
      for row in rows:
          collist.append(grid[row][column])
      problem.addConstraint(AllDifferentConstraint(), collist)
      collist = []

  for row in [0,3,6]: #Add uniqueness constraint for each house
      for column in [0,3,6]:
          problem.addConstraint(AllDifferentConstraint(), [grid[row][column],   grid[row+1][column],   grid[row+2][column],\
                                                           grid[row][column+1], grid[row+1][column+1], grid[row+2][column+1],\
                                                           grid[row][column+2], grid[row+1][column+2], grid[row+2][column+2]])

  for (x,y) in puzzle:
    problem.addConstraint(ExactSumConstraint(x), y)
  
  solution = problem.getSolution()

  #pretty printing of solved puzzle
  result = '+ - - - + - - - + - - - +\n'
  for row in rows:
    result += '| '
    for column in cols:
        result += str(solution[grid[row][column]]) + ' '
        if column %3 == 2:
            result += '| '
    result+= '\n'
    if row %3 == 2:
        result += '+ - - - + - - - + - - - +\n'
    
  return (result)
  
def extractpuzzle(puzzlestring):
  x = 0
  puzzle = []
  for i in puzzlestring:
    if i > 0:
      puzzle.append(int(i), (int(x/9), x%9))


def main():
  parser = argparse.ArgumentParser(description='Find Sudoku puzzle solution')
  #add mutually exclusive group (https://docs.python.org/3/library/argparse.html#mutual-exclusion)
  parser.add_argument('-p', '--puzzle', dest='puzzlestring', help='81 digit puzzle string')
  parser.add_argument('-i', '--input-file', dest='filename', help='a text file containing 1 or more 81 digit puzzle strings, separated by line breaks')
  args = parser.parse_args()
  
  if args.puzzlestring not null:
    print(solve(extractpuzzle(args.puzzlestring)))
  
if __name__ == '__main__':
   main()