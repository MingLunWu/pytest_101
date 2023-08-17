from typing import Dict
import time
import random

def call_external_api() -> Dict:
    """模擬呼叫外部的 API

    Returns:
        Dict: 外部 API 回傳的結果
    """
    time.sleep(0.5)
    # 有 50% 機率回傳沒有任何資料的 Dict
    if random.random() < 0.5:
        return {}
    response_value = random.random()
    return {"response_value": response_value}