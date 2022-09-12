---
html:
    toc: true
print_background: true
---

# MySQL 基本操作语句
`cmd + R` 调出控制台后，`cd` 至目录 `C:\Program Files\MySQL\MySQL Server 8.0\bin`，链接数据库后即可进行相关操作。

mysql 语句需以分号结尾才能正常运行。虽然 mysql 本身不区分大小写，但是在构建项目时大写 SQL 语句是一个良好的编程习惯。
```C
//进入 MySQL 控制台
mysql -u root -p
```
其中 `-u root` 表示使用 **root** 用户连接到服务器，`-p` 指示 mysql 提示输入密码。对于 Windows 系统而言，使用管理员账户绕过密码输入阶段直接访问数据库是一件比较危险的事，因此不推荐使用 `-pmysql` 而推荐 `-p`。密码验证通过后，输出栏显示 `mysql>` 前缀时表明进入了 MySQL 控制台。
```SQL
-- 退出控制台
EXIT
QUIT
ctrl + z
```

## 1. 数据库操作
```SQL
-- 显示数据库版本
SELECT version()

-- 预计结果：
+-----------+
| version() |
+-----------+
| 8.0.30    |
+-----------+
```

```SQL
-- 显示时间
SELECT now()

-- 预计结果：
+---------------------+
| now()               |
+---------------------+
| 2022-09-12 10:52:06 |
+---------------------+
```

```SQL
-- 查看所有数据库
SHOW DATABASES

-- 预计结果：
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| test               |
| world              |
+--------------------+
```

```SQL
-- 创建数据库
-- 新建名为 xxxx 的数据库。当名字中包含了“-”符号时，创建是没问题的，但是后期调用、删除的时候可能会出现名称索引问题。
-- 例如 `wqy-brynhildr`，只需在名称前后添加 “``” 即可。
-- 默认情况下编码格式为 latin，当输入中文字符时可能会出现乱码错误。因此最好使用 utf-8 或 gbk 格式编码数据。
CREATE DATABASE xxxx
CREATE DATABASE xxxx charset=utf8
```

#### 
```SQL
-- 查看创建的数据库信息
-- 显示数据库的名称、由什么命令创建、编码方式（gbk、utf-8 或 latin 等）
SHOW CREATE DATABASE xxxx

-- 查看 test 数据库的预计结果：
+----------+-------------------------------------------------------------------------------------------------+
| Database | Create Database                                                                                 |
+----------+-------------------------------------------------------------------------------------------------+
| test     | CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET gbk */ /*!80016 DEFAULT ENCRYPTION='N' */ |
+----------+-------------------------------------------------------------------------------------------------+
```

```SQL
-- 查看当前使用的数据库
SELECT DATABASE()

-- 在未使用 `USE` 语句之前，调用该命令的结果是：
+------------+
| database() |
+------------+
| NULL       |
+------------+

-- 使用 use 选定数据库后，`NULL` 将变为该数据库名称。
```

```SQL
-- 使用指定的数据库
USE xxxx
```

```SQL
-- 删除数据库（慎用）
DROP DATABASE xxxx
```

---
## 2. 数据表操作
### 2.1 常用数值类型
**数值类型**
| 类型 | 字节大小 (bytes) | 有符号范围 (signed) | 无符号范围 (unsigned) |
| --- | --- | --- | --- |
| TINYINT | 1 | -128 ~ 127 | 0 ~ 255 |
| SMALLINT | 2 | -32768 ~ 32767 | 0 ~ 65535 |
| MEDIUMINT | 3 | -8388608 ~ 8388607 | 0 ~ 16777215 |
| INT/INTEGER | 4 | -214783648 ~ 214783647 | 0 ~ 4294967295 |
| BIGINT | 8 | -9223372036854775808 ~ 9223372036854775807 | 0 ~ 18446744073709551615 |

**字符串类型**
| 类型 | 字节大小 | 说明 |
| --- | --- | --- |
| CHAR | 0 ~ 255 | CHAR(x)：固定长度字符串，长度不足时将补空格 |
| VARCHAR | 0 ~ 255 | VARCHAR(x)：非固定长度字符串，支持长度不超过 x 的字符串 |
| TEXT | 0 ~ 65535 | 大文本，超过 4000 bytes 时推荐使用该数据格式 |

**日期时间类型**
| 类型 | 字节大小 | 示例 |
| --- | --- | --- |
| DATE | 4 | '2022-09-11' |
| TIME | 3 | '16:21:49' |
| DATETIME | 8 | '2022-09-11 16:21:49' |
| YEAR | 1 | '2022' |
| TIMESTAMP | 4 | '2022-09-10 16:21:49' UTC ~ '2022-09-11 16:21:49' UTC |

其它数据类型请参考 https://blog.csdn.net/anxpp/article/details/51284106/

### 2.2 数据表顶层操作
```SQL
-- 查看当前数据库中的所有表
SHOW TABLES

-- 以 sakila 数据库为例，在选中相关数据集后运行该命令，预计结果：
+----------------------------+
| Tables_in_sakila           |
+----------------------------+
| actor                      |
| actor_info                 |
| address                    |
| category                   |
| city                       |
| country                    |
| customer                   |
| customer_list              |
| film                       |
| film_actor                 |
| film_category              |
| film_list                  |
| film_text                  |
| inventory                  |
| language                   |
| nicer_but_slower_film_list |
| payment                    |
| rental                     |
| sales_by_film_category     |
| sales_by_store             |
| staff                      |
| staff_list                 |
| store                      |
+----------------------------+
```

```SQL
-- 创建数据表
-- 常用约束：
-- auto_increment: 自动增长
-- not null: 不允许为空
-- primary key: 主键
-- default: 默认值
-- 关键命令：
-- CREATE TABLE 数据表名称(字段 类型 约束[, 字段 类型 约束])
-- 相当于创建 classes 表(id, name)
CREATE TABLE xxxx(id INT, name VARCHAR(30))
```

```SQL
-- 以一个简单的病患信息数据库为例：
CREATE TABLE patient(
    id int unsigned PRIMARY KEY NOT NULL auto_increment,
    name varchar(30) NOT NULL,
    gender enum("male","female") NOT NULL DEFAULT "male",
    age tinyint unsigned NOT NULL,
    feature_1 decimal(9,4) NOT NULL,
    feature_2 decimal(9,4) NOT NULL
)
```

```SQL
-- 删除数据表（慎用）
DROP TABLE xxxx
```

```SQL
-- 查看数据表结构
DESC xxxx

-- 以新建的 patient 数据表为例，预计结果：
+-----------+-----------------------+------+-----+---------+----------------+
| Field     | Type                  | Null | Key | Default | Extra          |
+-----------+-----------------------+------+-----+---------+----------------+
| id        | int unsigned          | NO   | PRI | NULL    | auto_increment |
| name      | varchar(30)           | NO   |     | NULL    |                |
| gender    | enum('male','female') | NO   |     | male    |                |
| age       | tinyint unsigned      | NO   |     | NULL    |                |
| feature_1 | decimal(9,4)          | NO   |     | NULL    |                |
| feature_2 | decimal(9,4)          | NO   |     | NULL    |                |
+-----------+-----------------------+------+-----+---------+----------------+
```

### 2.3 修改表
```SQL
-- 修改表：添加字段
-- xxxx（表名），yy（列名），zz（类型），ww（约束）
ALTER TABLE xxxx ADD yy zz
ALTER TABLE patient ADD treatment_date datetime NOT NULL
```

```SQL
-- 修改表：删除字段
ALTER TABLE xxxx DROP yy
ALTER TABLE patient DROP feature_2
```

```SQL
-- 修改表：修改字段且重命名
-- xxxx（表名），yy_1（原列名），yy_2（新列名），zz（类型），ww（约束）
ALTER TABLE xxxx CHANGE yy_1 yy_2 zz ww
ALTER TABLE patient CHANGE feature_3 blood_pressure tinyint unsigned NOT NULL
```

```SQL
-- 修改表：修改字段，保留原名
-- xxxx（表名），yy（列名），zz（类型），ww（约束）
ALTER TABLE xxxx MODIFY yy zz ww
ALTER TABLE patient MODIFY treatment_date date NOT NULL
```

```SQL

```

```SQL

```

```SQL

```

```SQL

```

```SQL

```

```SQL

```
