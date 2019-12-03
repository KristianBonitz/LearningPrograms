import unittest

from 'xmas_code_day_2-1.py' import run_program

class Xmas_test(unittest.TestCase):
    def test_add(self):
        program = [1,0,0,3,99]
        self.assertEqual(run_program(program), [1,0,0,2,99])

    def test_multi(self):
        program = [2,0,0,3,99]
        self.assertEqual(run_program(program), [2,0,0,1,99])

    def test_multi2(self):
        program = [2,3,0,3,99]
        self.assertEqual(run_program(program), [2,3,0,6,99])

    def test_multi3(self):
        program = [2,4,4,5,99,0]
        self.assertEqual(run_program(program), [2,4,4,5,99,9801])

    def test_changing_operators(self):
        program = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(run_program(program), [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()
