# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2024/07/15
# @File:            test.py
# @Software:        Neovim 0.11.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------



import random

result = sorted(random.sample(range(1,36),5))
result.extend(sorted(random.sample(range(1,13),2)))
print(result)

