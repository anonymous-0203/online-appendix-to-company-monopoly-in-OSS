#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division

import os
import statistics
import numpy as np
import pymysql
from numpy import median
import pandas as pd

path = os.path.abspath('/Users/Yuxia/Desktop/monopoly/code/')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='openstack2019', charset='utf8')
cursor = conn.cursor()

# 计算每个repository总的commit数
with conn.cursor() as cursor:
    sql = 'select repository, count(distinct version) ' \
          'from commit_monopoly ' \
          'where version < 19 ' \
          'group by repository'
    cursor.execute(sql)
    repo_ver = cursor.fetchall()

dict_repo_ver = {}
for i in repo_ver:
    key = i[0]
    dict_repo_ver[key] = i[1]

analyzed_repos = np.loadtxt(path + "/data_fse/rq2_analyzed_repos.csv", delimiter=",", dtype=str, encoding='utf-8-sig')

vers = []
for i in analyzed_repos:
    print(type(i))
    ver = dict_repo_ver[i]
    vers.append(int(ver))

print(median(vers))
