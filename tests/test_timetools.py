# TEST FOR MODULE TIMETOOLS.PY

# Lets import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Test if dateiff function calculates correct and absolute values 
def test_datediff():
    assert timetools.datediff("2023-04-28","2023-04-10") == 18
    assert timetools.datediff("2023-04-10","2023-04-28") == 18

# Test if timeiff function calculates correct and absolute values 
def test_timediff():
    assert round(timetools.timediff("11:30:15", "10:10:05"),4) == 1.3361
    assert round(timetools.timediff("10:10:05", "11:30:15"),4) == 1.3361