from constraint import *

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

problem.addConstraint(ExactSumConstraint(1), ['0,8'])
problem.addConstraint(ExactSumConstraint(2), ['1,5'])
problem.addConstraint(ExactSumConstraint(3), ['1,7'])
problem.addConstraint(ExactSumConstraint(4), ['1,8'])
problem.addConstraint(ExactSumConstraint(5), ['2,1'])
problem.addConstraint(ExactSumConstraint(6), ['2,2'])
problem.addConstraint(ExactSumConstraint(4), ['3,4'])
problem.addConstraint(ExactSumConstraint(5), ['3,6'])
problem.addConstraint(ExactSumConstraint(4), ['4,2'])
problem.addConstraint(ExactSumConstraint(1), ['4,4'])
problem.addConstraint(ExactSumConstraint(7), ['5,1'])
problem.addConstraint(ExactSumConstraint(8), ['5,6'])
problem.addConstraint(ExactSumConstraint(6), ['6,3'])
problem.addConstraint(ExactSumConstraint(2), ['6,8'])
problem.addConstraint(ExactSumConstraint(8), ['7,3'])
problem.addConstraint(ExactSumConstraint(9), ['7,6'])
problem.addConstraint(ExactSumConstraint(4), ['8,0'])

solution = problem.getSolution()

#pretty printing of solved puzzle
result = "+ - - - + - - - + - - - +\n"
for row in rows:
  result += '| '
  for column in cols:
      result += str(solution[grid[row][column]]) + ' '
      if column %3 == 2:
          result += '| '
  result+= '\n'
  if row %3 == 2:
      result += "+ - - - + - - - + - - - +\n"
  
print (result)
