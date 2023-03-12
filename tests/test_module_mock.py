from src.module_mock import sleep_for_a_while, get_current_season, create_new_drink
from src.module_mock import Drink
from unittest.mock import Mock, patch
from datetime import datetime
import pytest
import time

@pytest.mark.skip
# 執行時會發現這個函數要跑非常久
def test_sleep_for_a_while():
    response = sleep_for_a_while(20)
    assert response==20

@pytest.mark.skip
def test_sleep_for_a_while_mock_func():
    with patch("src.module_mock.time.sleep"):
        response = sleep_for_a_while(20)
        assert response==20

@pytest.mark.skip
def test_sleep_for_a_while_replace_func():
    with patch("src.module_mock.time.sleep", new_callable=time.sleep(2)):
        response = sleep_for_a_while(20)
        assert response==20


# mock 某個套件，再手動定義 now 的回傳值
def test_get_current_season(mocker):
    mocker_datetime = mocker.patch("src.module_mock.datetime")
    mocker_datetime.now.return_value = datetime(2023, 5, 1, 0, 0, 0)
    season = get_current_season()
    assert season == "第二季"

# 使用 patch 裝飾子可以替換掉其他檔案的函數
@patch("src.module_mock.datetime")
def test_get_current_season_2(mock_datetime):
    mock_datetime.now.return_value = datetime(2023, 5, 1, 0, 0, 0) # 將 datetime.now() 的 return 替換成特定物件
    season = get_current_season()
    assert season == "第二季"

# patch 也可以以 context manager 的形式來替換
def test_get_current_season_3():
    with patch("src.module_mock.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 9, 1, 0, 0, 0)
        season = get_current_season()
        assert season == "第三季"

def test_create_drink():
    with patch.object(Drink, "get_price", return_value=50):
        drink = create_new_drink("soda", 20)
        assert drink.get_price() == 50
        assert drink.price==20

from src.module_mock import get_current_month

def test_get_current_month():
    with patch("src.module_mock.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023,4,1,0,0,0)
        month = get_current_month()
        assert month == 3