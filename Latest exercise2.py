# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


excel_file = "doing-economics-datafile-working-in-excel-project-2.xlsx"

# 读取整个表格
# usecols="A:Q"表示取A到Q列
# header=1表示表头在文件的第二行（索引从0开始）
# index_col="Period"表示将"Period"列作为索引列
data_np = pd.read_excel(
    excel_file,
    usecols="A:Q",
    header=1,
    index_col="Period",
)

# data_n 为无惩罚数据（行数约为前10行）
data_n = data_np.iloc[:10, :].copy()

# data_p 为有惩罚数据（行数约为第14行至第23行，即索引14:24）
data_p = data_np.iloc[14:24, :].copy()

# 将导入的数据类型转换为浮点数（double）
data_n = data_n.astype("double")
data_p = data_p.astype("double")

# 查看数据基本信息
print("Without punishment data (data_n):")
print(data_n.head())
print(data_n.info(), "\n")

print("With punishment data (data_p):")
print(data_p.head())
print(data_p.info(), "\n")

# 计算每一时期（行）的平均贡献
mean_n_c = data_n.mean(axis=1)
mean_p_c = data_p.mean(axis=1)

# 绘制平均贡献的折线图进行比较
fig, ax = plt.subplots()
mean_n_c.plot(ax=ax, label="Without punishment")
mean_p_c.plot(ax=ax, label="With punishment")
ax.set_title("Average contributions to the public goods game")
ax.set_ylabel("Average contribution")
ax.legend()
plt.show()

# 比较第一期和第十期的平均贡献，并绘制柱状图
compare_grps = pd.DataFrame(
    [mean_n_c.loc[[1,10]], mean_p_c.loc[[1,10]]],
    index=["Without punishment", "With punishment"]
)
compare_grps.columns = ["Round " + str(i) for i in compare_grps.columns]
compare_grps = compare_grps.T

compare_grps.plot.bar(rot=0)
plt.title("Average contribution in Round 1 and Round 10")
plt.ylabel("Average contribution")
plt.show()
