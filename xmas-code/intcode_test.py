import pytest

from intcode_comp import Intcode_Computer

def test_int_terminate():
    icc = Intcode_Computer([99,0,0,0,0])
    icc.run_all()
    assert icc.program == [99,0,0,0,0]

def test_int_add():
    icc = Intcode_Computer([1,0,0,0,99])
    icc.run_all();
    assert icc.program == [2,0,0,0,99]

def test_int_multi():
    icc = Intcode_Computer([2,4,0,0,99])
    icc.run_all();
    assert icc.program == [198,4,0,0,99]

def test_int_big_multi():
    icc = Intcode_Computer([2,4,4,5,99,0])
    icc.run_all();
    assert icc.program == [2,4,4,5,99,9801]

def test_int_big_program():
    icc = Intcode_Computer([1,1,1,4,99,5,6,0,99])
    icc.run_all();
    assert icc.program == [30,1,1,4,2,5,6,0,99]

def test_in_out_program():
    icc = Intcode_Computer([3,0,4,0,99],42)
    icc.run_all()
    assert icc.output == 42
