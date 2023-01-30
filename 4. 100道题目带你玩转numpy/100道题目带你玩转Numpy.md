---
html:
    toc: true
print_background: true
---

# 100 道题目带你玩转 Numpy

---

## 1-10

### 1. 导入 `numpy` 库并简写为 `np`
```python
import numpy as np
```

### 2. 查看 `numpy` 的版本和配置说明
```python
print(np.__version__)
np.show_config()
```

### 3. 创建一个长度为 10 的空向量
```python
x = np.empty(10)
print(x)
```

### 4. 找到任意数组的内存大小
```python
x = np.zeros((12,13))
print('The number of itmes in target variable: %d' %(x.size))
print('The size of each item in target variable: %d bytes' %(x.itemsize))
print('The size of taret variable: %d bytes' %(x.size * x.itemsize))
```

### 5. 查看 `numpy` 中 `add` 函数的说明文档
```python
np.info(np.add)
```

### 6. 创建一个长度为 10 且第五个值为 1 的零向量
```python
x = np.zeros((10))
x[4] += 1
print(x)
```

### 7. 创建一个值域范围从 10 到 49 的向量
```python
x = np.arange(10,50,1)
# np.arange(10,50)
print(x)
```

### 8. 反转一个向量
```python
x = np.arange(20)
x = x[::-1]
print(x)
```

### 9. 创建一个 $\mathbb{R}^{3 \times 3}$ 且取值范围从 0 到 8 的矩阵
```python
x = np.arange(9)
x = x.reshape(3,3)
print(x)
```

### 10. 找到数组 $[1,2,0,0,4,0]$ 中非 0 元素的位置索引
```python
x = np.array([1,2,0,0,4,0])
non_zero_idx = [idx for idx,item in enumerate(x) if item !=0]
print(non_zero_idx)
```