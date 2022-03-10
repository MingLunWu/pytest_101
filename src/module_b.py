from typing import Dict, Union

def update_value_by_key(origin_dict:Dict, key: str, value: Union[str, int, float]) -> Dict:
    """更新特定 Key 的 Value

    Args:
        origin_dict (Dict): Python 的 Dictionary
        key (str): 要被更新值的 Key
        value (Union[str, int, float]): 新的 Value

    Raises:
        KeyError: 當 Key 不存在時，拋出 KeyError

    Returns:
        Dict: 更新後的 Dictionary
    """
    if key not in origin_dict:
        raise KeyError
    
    new_dict = origin_dict
    new_dict[key] = value
    return new_dict

def check_key_exists(dictionary: Dict, key: str) -> bool:
    """確認特定的 Key 是否存在於 Dictionary 中

    Args:
        dictionary (Dict): 被檢查的 Dictionary
        key (str): 要確認的 Key

    Returns:
        bool: key 是否存在於 dictionary 中
    """
    if key in dictionary:
        return True
    else:
        return False