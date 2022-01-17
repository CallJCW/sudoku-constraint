import unittest
from unittest import mock
import argparse
from sudoku import *


class SudokuTests(unittest.TestCase):

  def test_sudoku_solve(self):
    self.assertEqual(solve('000000001000002034056000000000040500004010000070000800000600002000800900400000000'), '243986751987152634156473298628349517594718326371265849835691472712834965469527183')
    
    with self.assertRaises(SystemExit):
      solve('0a0000001000002034056000000000040500004010000070000800000600002000800900400000000') #includes non-digit
      
    with self.assertRaises(SystemExit):
      solve('00000001000002034056000000000040500004010000070000800000600002000800900400000000') #too few digits
      
    with self.assertRaises(SystemExit):
      solve('0000000100000203405600000000004050000401000007000080000060000200080090040000000011') #too many digits
        
    self.assertEqual(solve('500080049000500030067300001150000000000208000000000018700004150030002000490050003'), '513687249849521637267349581158463972974218365326795418782934156635172894491856723')
    self.assertEqual(solve('100007090030020008009600500005300900010080002600004000300000010040000007007000300'), '162857493534129678789643521475312986913586742628794135356478219241935867897261354')
    
  def test_sudoku_extractpuzzle(self):
    data = [(1, '0,8'), (2, '1,5'), (3, '1,7'), (4, '1,8'), (5, '2,1'), (6, '2,2'), (4, '3,4'), (5, '3,6'), (4, '4,2'), (1, '4,4'), (7, '5,1'), (8, '5,6'), (6, '6,3'), (2, '6,8'), (8, '7,3'), (9, '7,6'), (4, '8,0')]
    self.assertEqual(extractpuzzle('000000001000002034056000000000040500004010000070000800000600002000800900400000000'), data)
    
    with self.assertRaises(SystemExit):
      extractpuzzle('0a0000001000002034056000000000040500004010000070000800000600002000800900400000000') #includes non-digit
      
    with self.assertRaises(SystemExit):
      extractpuzzle('00000001000002034056000000000040500004010000070000800000600002000800900400000000') #too few digits

    with self.assertRaises(SystemExit):
      extractpuzzle('') #too few digits
      
    with self.assertRaises(SystemExit):
      extractpuzzle('0000000100000203405600000000004050000401000007000080000060000200080090040000000011') #too many digits
    
  def test_sudoku_prettysudoku(self):
    data = '+ - - - + - - - + - - - +\n'+\
           '| 5 1 3 | 6 8 7 | 2 4 9 | \n'+\
           '| 8 4 9 | 5 2 1 | 6 3 7 | \n'+\
           '| 2 6 7 | 3 4 9 | 5 8 1 | \n'+\
           '+ - - - + - - - + - - - +\n'+\
           '| 1 5 8 | 4 6 3 | 9 7 2 | \n'+\
           '| 9 7 4 | 2 1 8 | 3 6 5 | \n'+\
           '| 3 2 6 | 7 9 5 | 4 1 8 | \n'+\
           '+ - - - + - - - + - - - +\n'+\
           '| 7 8 2 | 9 3 4 | 1 5 6 | \n'+\
           '| 6 3 5 | 1 7 2 | 8 9 4 | \n'+\
           '| 4 9 1 | 8 5 6 | 7 2 3 | \n'+\
           '+ - - - + - - - + - - - +\n'
    self.assertEqual(prettysudoku('513687249849521637267349581158463972974218365326795418782934156635172894491856723'), data)

  def test_sudoku_main_p(self): #test -p option
    data ='+ - - - + - - - + - - - +\n'+\
          '| 1 6 2 | 8 5 7 | 4 9 3 | \n'+\
          '| 5 3 4 | 1 2 9 | 6 7 8 | \n'+\
          '| 7 8 9 | 6 4 3 | 5 2 1 | \n'+\
          '+ - - - + - - - + - - - +\n'+\
          '| 4 7 5 | 3 1 2 | 9 8 6 | \n'+\
          '| 9 1 3 | 5 8 6 | 7 4 2 | \n'+\
          '| 6 2 8 | 7 9 4 | 1 3 5 | \n'+\
          '+ - - - + - - - + - - - +\n'+\
          '| 3 5 6 | 4 7 8 | 2 1 9 | \n'+\
          '| 2 4 1 | 9 3 5 | 8 6 7 | \n'+\
          '| 8 9 7 | 2 6 1 | 3 5 4 | \n'+\
          '+ - - - + - - - + - - - +\n'

    with mock.patch('argparse.ArgumentParser.parse_args',\
                return_value=argparse.Namespace(\
                puzzlestring='100007090030020008009600500005300900010080002600004000300000010040000007007000300',\
                filename=None)) as mock_args:
      with mock.patch('builtins.print') as mock_print:
        main()
    mock_print.assert_called_with(data)
      
  def test_sudoku_main_f(self): #test -f option with test.txt
    data ='+ - - - + - - - + - - - +\n'+\
          '| 1 6 2 | 8 5 7 | 4 9 3 | \n'+\
          '| 5 3 4 | 1 2 9 | 6 7 8 | \n'+\
          '| 7 8 9 | 6 4 3 | 5 2 1 | \n'+\
          '+ - - - + - - - + - - - +\n'+\
          '| 4 7 5 | 3 1 2 | 9 8 6 | \n'+\
          '| 9 1 3 | 5 8 6 | 7 4 2 | \n'+\
          '| 6 2 8 | 7 9 4 | 1 3 5 | \n'+\
          '+ - - - + - - - + - - - +\n'+\
          '| 3 5 6 | 4 7 8 | 2 1 9 | \n'+\
          '| 2 4 1 | 9 3 5 | 8 6 7 | \n'+\
          '| 8 9 7 | 2 6 1 | 3 5 4 | \n'+\
          '+ - - - + - - - + - - - +\n'

    with mock.patch('argparse.ArgumentParser.parse_args',\
                return_value=argparse.Namespace(\
                puzzlestring= None,\
                filename='test.txt')) as mock_args:
      with mock.patch('builtins.print') as mock_print:
        main()
    mock_print.assert_has_calls([mock.call('Puzzle #1'),\
                                mock.call('162857493534129678789643521475312986913586742628794135356478219241935867897261354'),\
                                mock.call(data)])
  
if __name__ == '__main__':
    unittest.main()
    
    