import time
from datetime import datetime
from typing import Dict

def sleep_for_a_while(seconds: int) -> int:
    """模擬一個需要執行有點久的函數

    Args:
        seconds (int): Pending 時間


    Returns:
        int: 回傳 Pending 秒數
    """
    print("Ready for sleeping!")
    time.sleep(seconds)
    return seconds

def get_current_season() -> str:
    """根據當前日期回傳目前季度

    Returns:
        str: ["春季", "夏季", "秋季", "冬季"]
    """

    time_obj:datetime = datetime.now()
    
    month = time_obj.month

    if month // 4 == 0:
        return "第一季"
    elif month // 4 == 1:
        return "第二季"
    elif month // 4 == 2:
        return "第三季"
    elif month // 4 == 3:
        return "第四季"
    else:
        return f"month: {month}"

class Drink:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price
    
    @property
    def price(self):
        return self._price

    def get_price(self):
        return self._price

def create_new_drink(name: str, price: int) -> Drink:
    drink = Drink("Black Tea", price)
    return drink

def get_current_month() -> int:
    """回傳當下的月份

    Raises:
        Exception: 當月份發生錯誤時，回傳 Exception

    Returns:
        int: 執行當下的月份
    """
    today = datetime.now()

    month = today.month
    if month < 0:
        raise Exception("Wrong month")

    return today.month