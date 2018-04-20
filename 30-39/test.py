# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
x = np.random.normal(50, 10, 1000)

# ヒストグラムを出力
plt.hist(x)
plt.show()