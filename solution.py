import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(data: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t_statistic, p_value = ttest_1samp(data, 300)
    alpha = 0.02
    if p_value/2 < alpha and t_statistic < 0:
        return True # Отклоняем нулевую гипотезу
    else:
        return False # Не отклоняем нулевую гипотезу
