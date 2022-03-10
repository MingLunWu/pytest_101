import pytest
from src.module_a import square, concat

@pytest.mark.math
def test_square():
    assert square(8) == 64

@pytest.mark.string
def test_concat():
    str_1 = "Hello! "
    str_2 = "MingLun!"
    assert concat(str_1=str_1, str_2=str_2) == "Hello! MingLun!"

@pytest.mark.string
def test_concat_failed():
    str_1 = 555 # Error Type
    str_2 = 666 # Error Type
    with pytest.raises(TypeError, match="錯誤型態"):
        concat(str_1=str_1, str_2=str_2)