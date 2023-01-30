# -*- coding: utf-8 -*-
"""
@ author: Brynhildr Wu
@ email: brynhildrwu@gmail.com

update: 2023/01/19

"""

# %% load in modules
import torch

# %%
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

# %%
y = x.new_ones(5, 3, dtype=torch.float64)  # 返回的tensor默认具有相同的torch.dtype和torch.device
print(y)

z = torch.randn_like(x, dtype=torch.float) # 指定新的数据类型
print(z) 

# %%
