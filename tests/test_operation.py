from src.maths_operation import math_add,math_div,math_sub,math_mul
import pytest
# adding comments 
@pytest.fixture
def fixturetest():
    print("\npre test using fixture")
    yield
    print("\npost test using fixture")

def test_math_add(fixturetest):
    assert math_add(2,3)==5
        
def test_math_mul(fixturetest):
    assert math_mul(4,5)==20
    
def test_math_sub(fixturetest):
    assert math_sub(4,5)==-1
    
def test_math_div(fixturetest):
    assert math_div(5,5)==1.0
    
def test_math_div_2(fixturetest):
    with pytest.raises(ZeroDivisionError):
        math_div(55,0)
    