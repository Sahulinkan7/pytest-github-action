from src.maths_operation import math_add,math_div,math_sub,math_mul


def test_math_add():
    assert math_add(2,3)==5
    assert math_add(3,3)==6
    
def test_math_mul():
    assert math_mul(4,5)==20
    assert math_mul(5,7)==35
    
def test_math_sub():
    assert math_sub(4,5)==-1
    assert math_sub(99,90)==9
    
def test_math_div():
    assert math_div(5,5)==1.0
    assert math_div(10,2)==5.0
    assert math_div(18,3)==6.0
    