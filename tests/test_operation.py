from src.maths_operation import math_add,math_div,math_sub,math_mul
import pytest
import logging

logger=logging.getLogger(__name__)


# adding comments 
@pytest.fixture
def fixturetest():
    logger.info("pre test using fixture")
    yield "abc"
    logger.info("post test using fixture")
    
def test_math_add(fixturetest):
    logger.info(f"testing addition operation")
    assert math_add(2,3)==5
        
def test_math_mul(fixturetest):
    logger.info(f"testing multiplication operation")
    assert math_mul(4,5)==20
    
def test_math_sub(fixturetest):
    logger.info(f"testing subtraction operation")
    assert math_sub(4,5)==-1
    
def test_math_div(fixturetest):
    logger.info(f"testing division operation")
    assert math_div(5,5)==1.0
    
def test_math_div_2(fixturetest):
    logger.info(f"testing division 2 operation")
    with pytest.raises(ZeroDivisionError):
        math_div(55,0)
    