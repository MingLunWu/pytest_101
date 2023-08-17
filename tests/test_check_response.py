from src.check_response import check_response_greater_than_0_5
from pytest_mock import MockFixture
from unittest import mock
import pytest

# 使用 unittest 寫法
def test_check_response_greater_than_0_5_true():
    with mock.patch("src.check_response.call_external_api") as mock_api_1:
        mock_api_1.return_value = {"response_value": 0.95}
        result = check_response_greater_than_0_5()
        assert result is True

# 使用 pytest-mock 寫法
def test_check_response_greater_than_0_5_false(mocker: MockFixture):
    return_value = {"response_value": 0.25}
    mock_api_2 = mocker.patch("src.check_response.call_external_api", return_value=return_value)
    result = check_response_greater_than_0_5()
    assert result is False

# 使用 pytest-mock 寫法
def test_check_response_greater_than_0_5_error(mocker: MockFixture):
    return_value = {}
    mock_api_3 = mocker.patch("src.check_response.call_external_api", return_value=return_value)
    with pytest.raises(KeyError):
        check_response_greater_than_0_5() # 預期要拋出 KeyError