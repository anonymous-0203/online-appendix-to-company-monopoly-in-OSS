#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import os
import numpy as np
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
import pandas as pd
from scipy import stats
from scipy.stats import norm

# sns.set_theme(style="white")
# sns.set_palette("husl")

path = os.path.abspath('/Users/Yuxia/Desktop/monopoly/code/')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='openstack2019', charset='utf8')
cursor = conn.cursor()

# 'repo', 'num_com', 'sum_cmt', 'max_com', 'max_com_cmt', 'max_P', 'is_only_one', 'is_dominate'
domi_overall = np.loadtxt(path + "/data_fse/domination_overall1.csv", delimiter=",", dtype=str)
print('domi_overall', domi_overall)

domi_ratio = []
for i in domi_overall:
    if i[7] == 'Y':
        domi_ratio.append(float(i[5]))
print(median(domi_ratio))

# domi_overall.remove['repo', 'num_com', 'sum_cmt', 'max_com', 'max_com_cmt', 'max_P', 'is_only_one', 'is_dominate']
df_overall = pd.DataFrame(domi_overall, columns=['repo', 'num_com', 'sum_cmt', 'max_com', 'max_com_cmt',
                                                 'Max Code Authorship', 'is_only_one', 'is_dominate'])
df_overall['Max Code Authorship'] = df_overall['Max Code Authorship'].astype(float)

figsize = 6, 4
fig, ax = plt.subplots(figsize=figsize)
# plt.grid('off')
# sns.set_style = "white"
sns.histplot(data=df_overall, x='Max Code Authorship', kde=False, bins=[0, 0.2, 0.4, 0.6, 0.8, 1], color='#5B9BD5', alpha=0.8)
# plt.hist(data=df_overall, x='Max Code Authorship', bins=10, color='#5B9BD5')
plt.vlines(0.5, 0, 360, colors="black", linestyles="dashed")
# plt.xticks(range(1))
ax.text(0.1, 345, "Code Authorship = 0.5", color='red')
plt.ylabel('Number of repositories')
plt.savefig(path + "/pic_fse/Max Code Ownership_overall.pdf", format='pdf')
plt.show()

# 'repo', 'version', 'num_com', 'sum_cmt', 'max_com', 'max_com_cmt', 'max_P', 'is_only_one', 'is_dominate'
domi_version = np.loadtxt(path + "/data_fse/domination_version1.csv", delimiter=",", dtype=str)
df_version = pd.DataFrame(domi_version, columns=['repo', 'repo_type', 'version', 'real_ver', 'num_com', 'sum_cmt',
                                                 'max_com', 'max_com_cmt', 'max_P', 'is_only_one', 'is_dominate'])
df_version['version'] = df_version['version'].astype(int)
ratios = []
for i in range(6, 19):
    print(str(i))
    sum_repo = len(df_version.loc[(df_version.version == i)])
    domi_repo = len(df_version.loc[(df_version.version == i) & (df_version.is_dominate == 'Y')])

    ratio = domi_repo/sum_repo
    ratios.append([i, domi_repo, sum_repo, ratio])

df_ratios = pd.DataFrame(ratios, columns=['Version', 'Num_domi_repos', 'Num_all_repos',  'Percentage'])
print('df_ratios', df_ratios)

print('df_ratios.filter(items=[\'Version\'])', df_ratios.filter(items=['Version']))
print(median(df_ratios['Percentage'].values))

plt.rcParams['figure.figsize'] = (6, 4)
# plt.grid(zorder=0)  # 画网格
fig, ax1 = plt.subplots()
ax1.grid(zorder=0)
# 柱形的宽度
width = 0.4
# 柱形的间隔
x1_list = []
x2_list = []
x3_list = []
for i in range(6, 19):
    x1_list.append(i)
    x2_list.append(i + width)
    x3_list.append(i + width/2)

# sns.set_style("white")
# 绘制柱形图1
b1 = ax1.bar(x1_list, np.array(df_ratios['Num_domi_repos'].values), width=width, color='#5B9BD5', zorder=10)
# 绘制柱形图2
b2 = ax1.bar(x2_list, df_ratios['Num_all_repos'], width=width, color='#70AD47', zorder=10)
plt.legend(loc='upper left', labels=['Dominated', 'Total'], bbox_to_anchor=(0, 1.02), frameon=False)
plt.xticks([index + 0.2 for index in x1_list], ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"])
ax1.tick_params(axis='y', colors='black')
# 绘制折线图 --双Y轴
ax2 = ax1.twinx()
b3 = ax2.plot(x3_list, df_ratios['Percentage'], color='black', marker='o', linewidth=1, markersize=4)
# 坐标轴标签设置
ax1.set_xlabel('Version', fontsize=12)
ax1.set_ylabel('Number of repositories', fontsize=12)
ax2.set_ylabel('Domination Percentage', fontsize=12)
ax2.axis(ymin=0, ymax=1)
ax2.tick_params(axis='y', colors='black')
plt.legend(loc='upper left', labels=['Percentage'], bbox_to_anchor=(0, 0.9), frameon=False)
plt.savefig(path + "/pic_fse/Domination Percentage_each_ver.pdf", format='pdf')
plt.show()

