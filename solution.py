import pandas as pd
import numpy as np

from math import log
from scipy.stats import expon


chat_id = 955921869 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    za = expon.ppf(alpha / 2, scale=n)
    zb = expon.ppf(1 - alpha / 2, scale=n)
    loc = x.min()
    return (za + 0.5 + x.min()) / 71**2, \
           (zb + 0.5 + x.min()) / 71**2
