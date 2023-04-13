import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as w

chat_id = 753540521  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:  # Одна или две выборке на входе, заполняется исходя из условия

    _, pvalue = w.ztest(x, value=500, alternative='larger')

    return pvalue <= 0.05
