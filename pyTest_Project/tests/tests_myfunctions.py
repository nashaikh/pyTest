from _ast import Assert
from unittest import result

import pytest
import functions.my_functions as myFunctions

def test_add():
    result =  myFunctions.Add(1,5)
    assert result == 6



def test_divide():
    result = myFunctions.divide(2, 2)
    assert result == 1



