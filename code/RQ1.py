#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import os
import numpy as np
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
import pandas as pd
from scipy import stats
from scipy.stats import norm

path = os.path.abspath('/Users/***/Desktop/monopoly/code/')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='openstack2019', charset='utf8')
cursor = conn.cursor()

monopoly_version = np.loadtxt(path + "/data/monopoly_version.csv", delimiter=",", dtype=np.str)

# repo, ver, real_ver, num_cmt, com, num_ccmt, ratio, monopoly
df = pd.DataFrame(monopoly_version, columns=['repo', 'Version', 'N-version', 'num_cmt', 'com', 'num_ccmt', 'Ratio', 'monopoly'])
df['N-version'] = df['N-version'].astype(int)
df['Version'] = df['Version'].astype(int)
df['Ratio'] = df['Ratio'].astype(float)
print('df', df)


tips = sns.load_dataset("tips")
print('type of tips', tips)
print('tip', tips)


figsize = 10, 4
fig, ax = plt.subplots(figsize=figsize)
ax = sns.boxplot(x="N-version", y="Ratio", data=df, palette="coolwarm", showmeans=True)
ax.text(18.2, 0.485, "0.50", color='red')
plt.hlines(0.5, -0.5, 18.2, colors="black", linestyles="dashed")
plt.savefig(path + "/pic/distribution_of_ratio_over_survival_time.pdf", format='pdf')
plt.show()

figsize = 10, 4
fig, ax = plt.subplots(figsize=figsize)
sns.boxplot(x="Version", y="Ratio", data=df, palette="coolwarm", showmeans=True)
plt.ylabel("Ratio")
ax.text(18.2, 0.485, "0.50", color='red')
plt.hlines(0.5, -0.5, 18.2, colors="black", linestyles="dashed")
plt.savefig(path + "/pic/distribution_of_ratio_over_version.pdf", format='pdf')
plt.show()

# calculate the overall ratio of monopoly in all the repositories
monopoly_overall = np.loadtxt(path + "/data/monopoly_overall.csv", delimiter=",", dtype=np.str)
# repo, num_cmt, com, num_ccmt, ratio, monopoly
df_overall = pd.DataFrame(monopoly_overall, columns=['repo', 'num_cmt', 'com', 'num_ccmt', 'Ratio', 'monopoly'])
df_overall['Ratio'] = df_overall['Ratio'].astype(float)
print('df_overall', df_overall.head())
print('ratio\n', df_overall['Ratio'].sample(20))
figsize = 6, 4
fig, ax = plt.subplots(figsize=figsize)
sns.histplot(data=df_overall, x='Ratio', kde=True, bins=10)
plt.vlines(0.5, 0, 200, colors="black", linestyles="dashed")
ax.text(0.4, 220, "Ratio = 0.50", color='red')
plt.savefig(path + "/pic/ratio_in_repo_overall.pdf", format='pdf')
plt.show()

# display the distribution of companies with different number of monopolized repositories in each version
# this figure was drawn by excel






