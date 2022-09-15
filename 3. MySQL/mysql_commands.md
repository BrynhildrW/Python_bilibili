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
-- AUTO_INCREMENT: 自动增长
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
    id int unsigned PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name varchar(30) NOT NULL,
    gender enum("male","female") NOT NULL DEFAULT "male",
    age tinyint(3) unsigned NOT NULL,
    feature_1 decimal(9,4) NOT NULL,
    feature_2 decimal(9,4) NOT NULL
)
```

```SQL
-- 查看创建的数据表信息
SHOW CREATE TABLE xxxx

-- 预计结果
+---------+---------------------------------------------+
| Table   | Create Table                                |
+---------+---------------------------------------------+
| patient | CREATE TABLE `patient` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `gender` enum('male','female') NOT NULL DEFAULT 'male',
  `age` tinyint unsigned NOT NULL,
  `feature_1` decimal(9,4) NOT NULL,
  `feature_2` decimal(9,4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk                    |
+---------+--------------------------------------------+
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

```SQL
-- 查看表中的全部数据
SELECT * FROM xxxx
SELECT * FROM patient
```

### 2.3 修改表
```SQL
-- 修改表：添加字段
-- xxxx（表名），yy（列名），zz（类型），ww（约束）
ALTER TABLE xxxx ADD yy zz
ALTER TABLE patient ADD treatment_date datetime
```

```SQL
-- 修改表：删除字段（慎用）
ALTER TABLE xxxx DROP yy
ALTER TABLE patient DROP feature_2
```

```SQL
-- 修改表：修改字段且重命名
-- xxxx（表名），yy_1（原列名），yy_2（新列名），zz（类型），ww（约束）
ALTER TABLE xxxx CHANGE yy_1 yy_2 zz ww
ALTER TABLE patient CHANGE feature_1 blood_pressure tinyint(3) unsigned
```

```SQL
-- 修改表：修改字段，保留原名
-- xxxx（表名），yy（列名），zz（类型），ww（约束）
ALTER TABLE xxxx MODIFY yy zz ww
ALTER TABLE patient MODIFY treatment_date date
```

## 3 数据的增删改查（CURD）
### 3.1 数据新增
```SQL
-- 插入新数据（全字段新增）
-- xxxx（表名），args（各字段参数，按顺序排列）
INSERT INTO xxxx VALUES(*args)

-- 例如 patient 表
+----------------+-----------------------+------+-----+---------+----------------+
| Field          | Type                  | Null | Key | Default | Extra          |
+----------------+-----------------------+------+-----+---------+----------------+
| id             | int unsigned          | NO   | PRI | NULL    | auto_increment |
| name           | varchar(30)           | NO   |     | NULL    |                |
| gender         | enum('male','female') | NO   |     | male    |                |
| age            | tinyint unsigned      | YES  |     | NULL    |                |
| blood_pressure | tinyint unsigned      | YES  |     | NULL    |                |
| treatment_date | date                  | YES  |     | NULL    |                |
+----------------+-----------------------+------+-----+---------+----------------+

-- 关于主键位置的三种写法（结果一样）
INSERT INTO patient VALUES(0, 'Brynhildr', 'male', 25, 127, '2022-09-13')
INSERT INTO patient VALUES(NULL, 'Brynhildr', 'male', 25, 127, '2022-09-13')
INSERT INTO patient VALUES(DEFAULT, 'Brynhildr', 'male', 25, 127, '2022-09-13')

-- 对于 ENUM 枚举，可以通过数字（1-N）代替实际选项
INSERT INTO patient VALUES(0, 'Brynhildr', 1, 25, 127, '2022-09-13')

-- SELECT * FROM patient
+----+-----------+--------+-----+----------------+----------------+
| id | name      | gender | age | blood_pressure | treatment_date |
+----+-----------+--------+-----+----------------+----------------+
|  1 | Brynhildr | male   |  25 |            125 | 2022-09-13     |
+----+-----------+--------+-----+----------------+----------------+
```

```SQL
-- 插入新数据（部分字段新增）
INSERT INTO xxxx (yy_1,yy_2,...) VALUES(value_1, value_2,...)
INSERT INTO patient (name, gender, age) VALUES('Valkury', 2, 24)

-- SELECT * FROM patient
+----+-----------+--------+------+----------------+----------------+
| id | name      | gender | age  | blood_pressure | treatment_date |
+----+-----------+--------+------+----------------+----------------+
|  1 | Brynhildr | male   |   25 |            125 | 2022-09-13     |
|  2 | Valkury   | female |   24 |           NULL | NULL           |
+----+-----------+--------+------+----------------+----------------+
```

```SQL
-- 批量插入数据（部分字段新增）
-- 类似的方法同样可用于全字段新增
INSERT INTO patient (name, gender, age) VALUES('Odin', 1, 70),
                                              ('Hera', 2, 65)

-- SELECT * FROM patient
+----+-----------+--------+------+----------------+----------------+
| id | name      | gender | age  | blood_pressure | treatment_date |
+----+-----------+--------+------+----------------+----------------+
|  1 | Brynhildr | male   |   25 |            125 | 2022-09-13     |
|  2 | Valkury   | female |   24 |           NULL | NULL           |
|  3 | Odin      | male   |   70 |           NULL | NULL           |
|  4 | Hera      | female |   65 |           NULL | NULL           |
+----+-----------+--------+------+----------------+----------------+
```

### 3.2 数据修改
```SQL
-- 修改整列数据字段
-- xxxx（表名），yy_1,..（列名），values_1,...（值）
UPDATE xxxx SET yy_1=value_1, yy_2=value_2,...

-- 按索引条件修改个别数据字段
UPDATE xxxx SET yy_1=value_1, yy_2=value_2,... WHERE condition
UPDATE patient SET age=80 WHERE id=3

-- WHERE 条件索引不止适用于 UPDATE，同样适用于 SELECT
-- SELECT * FROM patient WHERE gender='male'
+----+-----------+--------+------+----------------+----------------+
| id | name      | gender | age  | blood_pressure | treatment_date |
+----+-----------+--------+------+----------------+----------------+
|  1 | Brynhildr | male   |   25 |            125 | 2022-09-13     |
|  3 | Odin      | male   |   80 |           NULL | NULL           |
+----+-----------+--------+------+----------------+----------------+
```

### 3.3 数据查询
```SQL
-- 基本查询（全部字段信息）
-- xxxx（表名）
SELECT * FROM xxxx WHERE condition
SELECT * FROM patient WHERE gender='male'

-- 预计结果
+----+-----------+--------+------+----------------+----------------+
| id | name      | gender | age  | blood_pressure | treatment_date |
+----+-----------+--------+------+----------------+----------------+
|  1 | Brynhildr | male   |   25 |            125 | 2022-09-13     |
|  3 | Odin      | male   |   80 |           NULL | NULL           |
+----+-----------+--------+------+----------------+----------------+
```

```SQL
-- 查询指定列（部分字段）
-- xxxx（表名），yy_1,...（列名），condition（条件）
SELECT yy_1,yy_2,... FROM xxxx WHERE condition
SELECT name,gender FROM patient WHERE id<3

-- 预计结果
+-----------+--------+
| name      | gender |
+-----------+--------+
| Brynhildr | male   |
| Valkury   | female |
+-----------+--------+
```

```SQL
-- 查询的同时，为列指定暂用的别名
-- xxxx（表名），yy_1,...（列名）
-- 顺序可以自定义，允许不与表字段顺序一致
SELECT yy_1 AS yy_new1, yy_2 AS yy_new2,... FROM xxxx
SELECT gender AS 性别, name AS 姓名 FROM patient

-- 预计结果
+--------+-----------+
| 性别   | 姓名      |
+--------+-----------+
| male   | Brynhildr |
| female | Valkury   |
| male   | Odin      |
| female | Hera      |
+--------+-----------+
```

### 3.4 数据删除（慎用）
```SQL
-- 物理删除（全删，删库跑路）
-- xxxx（表名）
DELETE FROM xxxx

-- 删除部分无用字段
-- xxxx（表名），yy_1,...（列名）
DELETE FROM xxxx WHERE condition
```

```SQL
-- 逻辑删除，实际数据还在
-- 用一个额外字段表示该数据是否继续使用
-- xxxx（表名），is_delete 二元属性，默认为 0，即保留
ALTER TABLE xxxx ADD is_delete bit DEFAULT 0
ALTER TABLE patient ADD is_delete bit DEFAULT 0
UPDATE patient SET is_delete=1 WHERE id=1

-- 预计结果
+----+-----------+--------+------+----------------+----------------+----------------------+
| id | name      | gender | age  | blood_pressure | treatment_date | is_delete            |
+----+-----------+--------+------+----------------+----------------+----------------------+
|  1 | Brynhildr | male   |   25 |            125 | 2022-09-13     | 0x01                 |
|  2 | Valkury   | female |   24 |           NULL | NULL           | 0x00                 |
|  3 | Odin      | male   |   80 |           NULL | NULL           | 0x00                 |
|  4 | Hera      | female |   65 |           NULL | NULL           | 0x00                 |
+----+-----------+--------+------+----------------+----------------+----------------------+
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
