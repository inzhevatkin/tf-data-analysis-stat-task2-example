import pandas as pd
import numpy as np

from math import log
from scipy.stats import expon


chat_id = 955921869 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x);
    alfa = (1-p)/2;
    za = -log(1-alfa)/n;
    zb = -log(alfa)/n;
    loc = x.min()
    t=71**2;
    return (za - 0.5 + loc)/t, \
           (zb - 0.5 + loc)/t
