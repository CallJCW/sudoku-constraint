import argparse
import os
from constraint import *

def prettysudoku(puzzlestring):
  cols = range(9)
  rows = range(9)

  result = '+ - - - + - - - + - - - +\n'
  for row in rows:
    result += '| '
    for column in cols:
        result += str(puzzlestring[row*9+column]) + ' '
        if column %3 == 2:
            result += '| '
    result+= '\n'
    if row %3 == 2:
        result += '+ - - - + - - - + - - - +\n'
        
  return (result)
  
def extractpuzzle(puzzlestring):
  x = 0
  puzzle = []
  if len(puzzlestring) != 81:
    raise SystemExit('Exception in extractpuzzle(puzzlestring): puzzlestring not valid length: ' + str(len(puzzlestring) ) + ' ' + puzzlestring)
  else:
    for i in puzzlestring:
      if i.isdigit():
        if int(i) > 0:
          puzzle.append((int(i), (str(int(x/9)) + ',' + str(x%9) ) ) )
      else:
        raise SystemExit('Exception in extractpuzzle(puzzlestring): character number ' + str(x)  + ' "' + i + '" is not a digit ' + puzzlestring)
      x += 1
      
  return (puzzle)

def solve(puzzlestring):
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

  puzzle = extractpuzzle(puzzlestring)
  for (x,y) in puzzle:
    problem.addConstraint(ExactSumConstraint(x), [y])
  
  solution = problem.getSolution()
  
  if solution:
    solvedpuzzlestring = ''
    for row in rows:
      for column in cols:
          solvedpuzzlestring += str(solution[grid[row][column]])
  else:
    raise SystemExit('puzzlestring does not describe a valid sudoku puzzle: ' + puzzlestring)

  return (solvedpuzzlestring)

def main():
  parser = argparse.ArgumentParser(description='Find Sudoku puzzle solution')
  #add mutually exclusive group (https://docs.python.org/3/library/argparse.html#mutual-exclusion)
  parser.add_argument('-p', '--puzzle', dest='puzzlestring', help='81 digit puzzle string')
  parser.add_argument('-f', '--file', dest='filename', help='a text file containing 1 or more 81 digit puzzle strings, separated by line breaks')
  args = parser.parse_args()
  
  if args.puzzlestring:
    if len(args.puzzlestring) != 81:
      #print('puzzlestring not valid length', args.puzzlestring)
      raise SystemExit('puzzlestring not valid length: ' + str(len(args.puzzlestring) ) + ' ' + args.puzzlestring)
    else:
      print(prettysudoku(solve(args.puzzlestring)))
  if args.filename:
    if not os.path.isfile(args.filename):
      #print('File does not exist')
      raise SystemExit('File does not exist')
    else:
      with open(args.filename, 'r') as file:
        linenumber = 1
        for line in file.readlines():
          line = line.strip()
          if len(line) != 81:
            #print('puzzlestring not valid length', str(len(line) ), line)
            raise SystemExit('Line: ' + str(linenumber) + ' puzzlestring not valid length: ' + str(len(line) ) + ' ' + line)
          else:
            print('Puzzle #' + str(linenumber))
            print(solve(line))
            print(prettysudoku(solve(line)))
          linenumber += 1
  
if __name__ == '__main__':
   main()