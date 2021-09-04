#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import os
import numpy as np
import pandas as pd
import pymysql
import random
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
import pandas as pd
from scipy import stats
from scipy.stats import norm
from pandas.core.frame import DataFrame

path = os.path.abspath('/Users/***/Desktop/monopoly/code/')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='openstack2019', charset='utf8')
cursor = conn.cursor()

# repo, ver, real_ver, num_cmt, com, num_ccmt, ratio, monopoly
monopoly_version = np.loadtxt(path + "/data/monopoly_version.csv", delimiter=",", dtype=np.str)

# sampling repositories to manual analyze
monopolized_repo = []
for i in monopoly_version:
    print(i)
    repo = i[0]
    repo_type = i[1]
    monopoly = i[8]

    if monopoly == 'yes' and [repo, repo_type] not in monopolized_repo:
        monopolized_repo.append([repo, repo_type])

print('len(monopolized_repo)', len(monopolized_repo))
np.savetxt(path + "/data/monopolized_repo.csv", monopolized_repo, fmt="%s", delimiter=",")
monopolized_repo = DataFrame(monopolized_repo, columns=['repo', 'repo_type'])

repo_deployment = np.array(monopolized_repo[monopolized_repo.repo_type == 'deployment']).tolist()
repo_component = np.array(monopolized_repo[monopolized_repo.repo_type == 'component']).tolist()
repo_Client = np.array(monopolized_repo[monopolized_repo.repo_type == 'Client']).tolist()
repo_community = np.array(monopolized_repo[monopolized_repo.repo_type == 'community']).tolist()
repo_plugin = np.array(monopolized_repo[monopolized_repo.repo_type == 'plugin']).tolist()
repo_tools = np.array(monopolized_repo[monopolized_repo.repo_type == 'infra tools']).tolist()

sum_sampled_repos = 291
sum_repos = 1194

# dpl =

# 设置种子使得每次抽样结果相同
random.seed(10)

sampled_deployment_repos = random.sample(repo_deployment, int(len(repo_deployment)/1194*291))
sampled_component_repos = random.sample(repo_component, int(len(repo_component) / 1194 * 291))
sampled_client_repos = random.sample(repo_Client, int(len(repo_Client) / 1194 * 291))
sampled_community_repos = random.sample(repo_community, int(len(repo_community) / 1194 * 291 + 1))
sampled_plugin_repos = random.sample(repo_plugin, int(len(repo_plugin) / 1194 * 291 + 1))
sampled_tool_repos = random.sample(repo_tools, int(len(repo_tools) / 1194 * 291 + 1))

sampled_repos = sampled_deployment_repos + sampled_component_repos + sampled_client_repos + sampled_community_repos + \
                sampled_plugin_repos + sampled_tool_repos

print(sampled_repos)
print('len(sampled_repos)', len(sampled_repos))

data_for_manual_analyzing = []
for i in monopoly_version:
    repo = i[0]
    repo_type = i[1]

    if [repo, repo_type] in sampled_repos:
        data_for_manual_analyzing.append(i)
        print(i)

# np.savetxt(path + "/data/sampled_monopolized_repo.csv", sampled_repos, fmt="%s", delimiter=",")
np.savetxt(path + "/data/repos_for_manual_analyzing_whole.csv", data_for_manual_analyzing, fmt="%s", delimiter=",")


