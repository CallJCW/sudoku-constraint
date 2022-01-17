# sudoku-constraint

Sudoku solver using python-constraint (https://stackabuse.com/constraint-programming-with-python-constraint/)

Takes an 81 digit puzzle string from the command line or any number of such strings from a file, and prints the solution(s) in a pretty grid.

Puzzle strings contain zeroes for empty cells

### For example 

```python3 sudoku.py -p 100007090030020008009600500005300900010080002600004000300000010040000007007000300```

produces output of 
```
+ - - - + - - - + - - - +
| 1 6 2 | 8 5 7 | 4 9 3 |
| 5 3 4 | 1 2 9 | 6 7 8 |
| 7 8 9 | 6 4 3 | 5 2 1 |
+ - - - + - - - + - - - +
| 4 7 5 | 3 1 2 | 9 8 6 |
| 9 1 3 | 5 8 6 | 7 4 2 |
| 6 2 8 | 7 9 4 | 1 3 5 |
+ - - - + - - - + - - - +
| 3 5 6 | 4 7 8 | 2 1 9 |
| 2 4 1 | 9 3 5 | 8 6 7 |
| 8 9 7 | 2 6 1 | 3 5 4 |
+ - - - + - - - + - - - +
```
