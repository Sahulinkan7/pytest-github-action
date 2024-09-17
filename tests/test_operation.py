from src.maths_operation import math_add,math_div,math_sub,math_mul


def test_math_add():
    assert math_add(2,3)==5
    assert math_add(3,3)==6
    
def test_math_mul():
    assert math_mul(4,5)==20
    assert math_mul(5,7)==35