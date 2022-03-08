from typing import Type


def square(num: int) -> int:
    """範例函式，回傳平方值

    Args:
        num (int): 數值

    Returns:
        int: 平方後的數值
    """
    return num**2

def concat(str_1: str, str_2: str) -> str:
    """將兩個字串串接在一起

    Args:
        str_1 (str): 字串 1
        str_2 (str): 字串 2

    Raises:
        TypeError: 當任一參數不為 str 時，拋出 TypeError

    Returns:
        str: str_1+str_2
    """
    if not (isinstance(str_1, str) and isinstance(str_2, str)):
        raise TypeError("錯誤型態")
    else:
        return str_1 + str_2