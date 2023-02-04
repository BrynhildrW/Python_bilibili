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
x = np.arange(9).reshape(3,3)
print(x)
```

### 10. 找到数组 $[1,2,0,0,4,0]$ 中非 0 元素的位置索引
```python
x = np.array([1,2,0,0,4,0])
non_zero_idx = [idx for idx,item in enumerate(x) if item !=0]
print(non_zero_idx)
```

---

## 11-20
### 11. 创建一个 $\mathbb{R}^{3 \times 3}$ 的单位矩阵
```python
x = np.eye(3)
print(x)
```

### 12. 创建一个 $\mathbb{R}^{3 \times 3 \times 3}$ 的随机数组
```python
x = np.random.random((3,3,3))
print(x)
```

### 13. 创建一个随机数组 $\pmb{X} \in \mathbb{R}^{10 \times 10}$ 并求最值
```python
x = np.random.random((10,10))
x_max, x_min = np.max(x), np.min(x)
print('Maximum: {}\nMinimun: {}'.format(str(x_max), str(x_min)))
```

### 14. 创建一个长度为 30 的随机向量并求平均值
```python
x = np.random.random(30)
print(x.mean())
```

### 15. 创建一个二维数组，其中边界值为 1，其余为 0
```python
x = np.ones((10,10))
x[1:-1,1:-1] = 0
print(x)
```

### 16. 对于已有二维数组，添加一个用 0 填充的边界
```python
x = np.random.random((3,4))
# y = np.zeros((x.shape[0]+2, x.shape[1]+2))
# y[1:-1,1:-1] = x
y = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)
print(y)
```

### 17. 下列表达式的结果是什么
```python
0 * np.nan  # nan
np.nan == np.nan  # false
np.inf > np.nan  # false
np.nan - np.nan  # nan
0.3 == 3*0.1  # false
```

### 18. 创建一个 $\pmb{X} \in \mathbb{R}^{5 \times 5}$，设置主对角线下方元素为 1、2、3、4
```python
x = np.random.random((5,5))
for i in range(4):
    x[i+1,i] = i+1
print(x)
```

### 19. 创建一个 $\pmb{X} \in \mathbb{R}^{8 \times 8}$，且设为“0-1”棋盘格模式
```python
x = np.zeros((8,8))
# y = np.ones((8,8))
for i in range(8):
    for j in range(8):
        if (i+j)%2:
            x[i,j]=1
#             y[i,j]=0
print(x)
# print(y)
```

### 20. 已有 $\pmb{X} \in \mathbb{R}^{6 \times 7 \times 8}$，求第 100 个元素的索引
```python
np.unravel_index(100, (6,7,8))
```

---

## 21-30
### 21. 用 `tile` 函数创建一个棋盘格矩阵 $\pmb{X} \in \mathbb{R}^{8 \times 8}$
```python
x = np.tile(np.array([[1,0],[0,1]]), (4,4))
# x = np.tile(np.array([[0,1],[1,0]]), (4,4))
print(x)
```

### 22. 归一化随机矩阵 $\pmb{X} \in \mathbb{R}^{5 \times 5}$
```python
x = np.random.random((5,5))
norm_x = (x-np.min(x))/(np.max(x)-np.min(x))
print(norm_x)
```

### 23. 创建一个将颜色描述为（RGBA）四个无符号字节的自定义 `dtype`
```python
color = np.dtype([
    ('r', np.ubyte),
    ('g', np.ubyte),
    ('b', np.ubyte),
    ('a', np.ubyte)
])
color
```

### 24. 对 $\pmb{X} \in \mathbb{R}^{5 \times 3}$ 和 $\pmb{Y} \in \mathbb{R}^{3 \times 2}$ 实现 $\pmb{XY}$
```python
x = np.random.random((5,3))
y = np.random.random((3,2))
x @ y
```

### 25. 对给定一维数组在 3 至 8 之间（不含边界）的所有元素取反
```python
x = np.arange(0, 10, 0.5)
np.random.shuffle(x)
x[(x>3) & (x<8)] *= -1
print(x)
```

### 26. 下列脚本运行后结果为？
```python
# built-in add method, sum(iterable, start)
print(sum(range(5), -1))  # 9

# numpy.add method, add(data, axis, ...)
from numpy import *
print(sum(range(5), -1))  # 10
```

### 27. 对于整数向量 $\pmb{Z}$，下列表达合法的是？
```python
z = np.array([1,2,3,4,5,6,7,8,9,10])

z**z  # z[i]**z[i]
2 << z >> 2  # 2**z[i]
z <- z  # z[i]<-z[i]? True or False
1j * z  # complex array: 0 + jz
z/1/1  # z[i]/1
# z<z>z  # illegal
```

### 28. 下列表达式的结果分别为？
```python
np.array(0) / np.array(0)  # nan
np.array(0) // np.array(0)  # 0
np.array([np.nan]).astype(int).astype(float)  # array([-2.14748365e+09])
```

### 29. 如何从零位对浮点数组做舍入？
```python
x = np.random.uniform(-10,+10,10)
print(np.ceil(np.abs(x), x))
```

### 30. 找到两个数组中的共同元素
```python
x = np.random.randint(0,10,10)
y = np.random.randint(0,10,10)
print(np.intersectld(x, y))
```

---

## 31-40
### 31. 如何忽略所有的 `numpy` 警告 | （慎用）
```python
defaults = np.seterr(all='ignore')
data = np.ones(1)/0
```

### 32.下面的表达式正确吗？
```python
np.sqrt(-1) == np.emath.sqrt(-1)  # False: nan != 1j
```

### 33. 获取昨日、今日和明日的日期
```python
print('Yesterday is %s' %(np.datetime64('today', 'D') - np.timedelta64(1, 'D')))
print('Today is %s' %(np.datetime64('today', 'D')))
print('Tomorrow is %s' %(np.datetime64('today', 'D') + np.timedelta64(1, 'D')))
```

### 34. 得到所有与 2023 年 2 月对应的日期
```python
date_info = np.arange('2023-02', '2023-03', dtype='datatime64[D]')
print(date_info)
```

### 35. 在位计算 $A+B$ 、$-A/2$
```python
a = np.random.random(5)
b = np.random.random(5)

print('Original b: %s' %(str(b)))
print('Operate a+b then save it into b: %s' %(str(np.add(a, b, out=b))))
print('New b: {}'.format(str(b)))

print('\nOriginal a: %s' %(str(a)))
print('Operate -a/2 then save it into a: %s' %(str(np.divide(a, -2, out=a))))
print('New a: %s' %(str(a)))
```

### 36. 用五种不同方法提取随机数组的整数部分
```python
x = np.random.uniform(0,10,10)
print(x)

print(x - x%1)
print(np.floor(x))
print(np.ceil(x) - 1)
print(x.astype(int))
print(np.trunc(x))
```

### 37. 创建一个矩阵 $\pmb{X} \in \mathbb{R}^{5 \times 5}$，其中每行的数值范围均为 0 至 4
```python
x = np.zeros((5,5))
x += np.arange(5)
print(x)
```

### 38. 创建一个可生成 10 个整数的函数并构建数组
```python
def func():
    for i in range(10):
        yield i
x = np.fromiter(func(), dtype=float)
print(x)
```

### 39. 创建一个长度为 10 的随机向量，值域范围 $(0,1)$
```python
x = np.random.uniform(0,1,10)
print(x)
```

### 40. 创建一个长度为 10 的随机向量并排序
```python
x = np.random.random(10)
print('Original order: %s' %(str(x)))

x.sort()
print('Ascending order: %s' %(str(x)))
print('Descending order: %s' %(str(x[::-1])))
```

---

## 41-50
### 41. 对一个小数组用比 `np.sum` 更快的方式求和
```python
x = np.arange(10)
print(np.add.reduce(x))
```

### 42. 检查两个随机数组 a 和 b 是否相等
```python
a = np.random.random(10)
b = np.random.random(10)
print(np.allclose(a,b))
# print(np.array_equal(a,b))
```

### 43. 创建一个只读数组
```python
x = np.random.random(10)
x.flags.writeable = False
try:
    x[0] = 1
except ValueError:
    print('Target variable is read-only!')
```

### 44. 将笛卡尔坐标下的一个矩阵 $\pmb{X} \in \mathbb{R}^{10 \times 2}$ 转换为极坐标形式
```python
x = np.random.random((4,2))
print(x)

pos_x, pos_y = x[:,0], x[:,1]  # (x,y)

# (x,y) -> (r,theta)
x_new = np.zeros_like(x)
x_new[:,0] = np.sqrt(pos_x**2 + pos_y**2)  # r
x_new[:,1] = np.arctan2(pos_y, pos_x)  # theta(rad)
print(x_new)
```

### 45. 创建一个长度为 10 的向量，将最大值替换为 1
```python
x = np.random.random(10)
print(x)

x[np.argmax(x)] = 1
print(x)
```

### 46. 创建一个二维坐标数组，覆盖四边形区域 $[0,0],[0,1],[1,0],[1,1]$
```python
x_num, y_num = 3,4
square = np.ones((x_num,y_num), [('x',float), ('y',float)])
square['x'], square['y'] = np.meshgrid(np.linspace(0,1,y_num),
                                       np.linspace(0,1,x_num))  # row,column
print(square)
```

### 47. 给定向量 $\pmb{x}$ 和 $\pmb{y}$，构建 Cauchy 矩阵 $\pmb{C}$：$\pmb{C}(i,j)=\dfrac{1}{\pmb{x}(i)-\pmb{y}(j)}$
```python
x = np.random.random(3)
y = np.random.random(4)

# method 1
# 8.1 µs ± 63.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
C = np.zeros((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        C[i,j] = 1/(x[i]-y[j])

# method 2
# 4.42 µs ± 787 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
C = 1.0/np.subtract.outer(x,y)
```

### 48. 打印每个 `numpy` 标量类型的最大值和最小值
```python
for dtype in [np.int8, np.int32, np.int64]:
    print('%s | Min: %d; Max: %d' %(
        dtype,
        np.iinfo(dtype).min,
        np.iinfo(dtype).max
    ))

for dtype in [np.float32, np.float64]:
    print('%s | Min: %d; Max: %d' %(
        dtype,
        np.finfo(dtype).min,
        np.finfo(dtype).max
    ))
```

### 49. 打印数组中的所有数值
```python
import sys
np.set_printoptions(threshold=sys.maxsize)
x = np.ones((10,10))
print(x)
```

### 50. 给定标量后找到数组中最接近标量的值
```python
x = np.arange(100)
y = np.random.uniform(0,100)
index = np.argmin(abs(x-y))
print('Target value: %s' %(str(y)))
print('Nearest value (%sth): %s' %(str(index+1), str(x[index])))
```

---

## 51-60
### 51. 创建一个表示位置 (x,y) 和颜色 (r,g,b) 的结构化数组
```python
data = np.zeros(
    shape=10,
    dtype=[('position',[('x',float),
                        ('y',float)]),
           ('color',[('r',int),
                     ('g',int),
                     ('b',int)])]
)
print(data)
```

### 52. 对一个表示坐标形状为 (5,2) 的随机向量，找到两点间的距离
```python
x = np.random.random((5,2))
pos_x, pos_y = np.atleast_2d(x[:,0], x[:,1])
dist = np.sqrt((pos_x-pos_x.T)**2 + (pos_y-pos_y.T)**2)
print(dist)
```

### 53. 将 32 位的浮点数 (float) 转换为对应的整数 (integer)
```python
x = np.arange(10, dtype=np.int32)
print(x.astype(np.float32, copy=False))
```

### 54. 识别读取 txt 文件中的字符串数据
```python
from io import StringIO

s = StringIO(r'360102199701196319 wqy 3.14')  # use dtype to identify
data = np.genfromtxt(
    s,
    dtype=[('ID','S18'),('name','S10'),('myfloat','f8')],
    delimiter=' '
)
print(data)
```

### 55. 对于 `numpy` 数组，`enumerate`的等价操作
```python
x = np.arange(9).reshape(3,3)
for index, value in np.ndeumerate(data):
    print(index, value)
```

### 56. 生成一个通用的二维 Gaussian-like 数组
```python
pos_x, pos_y = np.meshgrid(np.linspace(-1,1,5), np.linspace(-1,1,5))
dist = np.sqrt(pos_x**2 + pos_y**2)
sigma, mu = 1.0, 0.0
g = np.exp(-(dist-mu)**2 / (2.0*sigma**2))
print(g)
```

### 57. 在一个二维数组内部随机放置 p 个元素
```python
n,p = 5,3
x = np.zeros((n,n))

# np.put(ndarray, target indices, value)
np.put(x, np.random.choice(range(n*n),p,replace=False), 5)
print(x)
```

### 58. 在矩阵中减去其每一行的均值
```python
x = np.random.random((3,4))
x -= x.mean(axis=1, keepdims=True)
print(x)
```

### 59. 基于二维数组的第 n 列对其每一行数据进行排序
```python
x = np.random.randint(0,10, (5,5))
n = 3
print(x)
print(x[x[:,n-1].argsort()])
```

### 60. 检查一个二维数组是否存在空列
```python
x = np.random.randint(0,10, (4,5))
print(x)
print(x.any(axis=0).any())  # True means full
```

---

## 61-70
### 61.
```python

```