import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 460411293 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = anderson_ksamp([x, y]).pvalue
    if p > 0.02:
       return False
    else:
        return True
