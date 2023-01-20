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
data = np.zeros((12,13))
print('The number of itmes in target variable: %d' %(data.size))
print('The size of each item in target variable: %d bytes' %(data.itemsize))
print('The size of taret variable: %d bytes' %(data.size * data.itemsize))
```

### 
