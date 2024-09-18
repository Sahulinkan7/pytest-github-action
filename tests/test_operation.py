from src.maths_operation import math_add,math_div,math_sub,math_mul
import pytest

def test_math_add():
    assert math_add(2,3)==5
        
def test_math_mul():
    assert math_mul(4,5)==20
    
def test_math_sub():
    assert math_sub(4,5)==-1
    
def test_math_div():
    assert math_div(5,5)==1.0
    
def test_math_div_2():
    with pytest.raises(ZeroDivisionError):
        math_div(55,0)
    