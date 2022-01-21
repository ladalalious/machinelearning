import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#数据集
path =  'ex1data1.txt'


# 读取数据
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
# 令x0=1
data.insert(0,'x_0',1)
print(data)
# data.head()
# data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))
# plt.show()

