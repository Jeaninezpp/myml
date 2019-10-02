# **MATLAB**基础知识

### 矩阵输入

- 直接输入法
  - 矩阵元素用空格，逗号分隔
  - 矩阵行用分号；分隔
  - 整个矩阵放在方括号里[ ]
  - 例如：[1,2,3;4,5,6;7,8,9;10,11,12]
- 变量
  - 变量名，函数名以字母打头，注意区分大小写．
  - who：检查内存变量
  - whos：检查驻留变量的详细情况
  - 永久变量，（预定义变量）eps,(最小正数)pi, inf, NaN, $i=j=\sqrt{-1}$（虚数单位）,flops(浮点运算次数，用于统计计算量)．不会被clear清除，
- 通用数理类函数
  - 基本数学函数
  - 特殊函数
  - 基本矩阵函数
  - 特殊矩阵函数
  - 矩阵分解和分析函数
  - 数据分析函数
  - 微分方程求解
  - 多项式函数
  - 非线性方程及其优化函数
  - 数值积分函数
  - 信号处理函数
- save load 保存变量和载入到工作区

### 数值计算

#### 创建数值矩阵

- av = 1:12　％产生以１－12为元素的**行向量**．
  - a=[1 2 3 4 5] %行向量
  - b=[1;2;3;4;5] %列向量
- bv = **reshape**(av,3,4)　％利用av创建3*4的矩阵bv
- **对角矩阵**
  - c=diag(cv)　％提取cv的对角线元素形成向量c
  - Ｃ=diag(c) 　％用向量c构成对角矩阵C

- 例子：

  - x=[1 2 3 4 5]
  - m=x<=3
    - m=[1 1 1 0 0]　％　ｍ是逻辑矩阵
  - x=x(m)
    - x=[1 2 3]　％　x是１＊３的矩阵

- **矩阵和数组运算**

  ![](/home/zpp/Documents/project/myml/mat/image/1569827242206.png)

  - 注意：
    - 左除\：a\b=inv(a)*b
    - 右除/：a/b=a*inv(b)

![](/home/zpp/Documents/project/myml/mat/image/basefun.png)

![](/home/zpp/Documents/project/myml/mat/image/Selection_012.png)

![Selection_011](/home/zpp/Documents/project/myml/mat/image/Selection_011.png)

- 解线性方程组
- 矩阵分解
  - LU
  - QR
  - Choleshy
- 多项式
- 符号计算
  - sym('x')	syms a b c x k t y
  - f=a*(2*x-t)^3+b\*sin(4\*y)
- 微积分计算
  - 导数
    - diff(f)
    - diff(f,t)
    - diff(f,2)
    - diff(f,t,2)
  - 积分
    - inf(f)　％函数ｆ对符号变量ｘ或接近字母ｘ的符号变量求不定积分．
    - inf(f,t)
    - inf(f,t,a,b)　%函数f对符号变量t求从a到b的定积分．
  - 极限
    - limit(f)
    - limit(f,t,a,'left'/'right')
  - 级数和：symsum(s,t,a,b)
  - 泰勒(Taylor)多项式：taylor(f,n,a)函数ｆ对符号变量x或者最接近x的符号变量在a点的n-1阶泰勒多项式(ｎ缺省时为６，ａ缺省时为０)
- 解方程
  - 代数方程
  - 微分方程
- 线性代数
- 化简和代换
  - collect %合并同类项
  - expand　％将乘积展开为和式
  - horner　％把多项式转化为嵌套表示形式
  - simplify　％利用各种恒等式化简代数式

### 可视化

#### 二维

- plot
  - plot(x,y)
  - plot(x,y1,x,y2,x,y3,x,y4,....)
  - plot(x,y1,'k:',x,y2,'b-')
  - ![](/home/zpp/Documents/project/myml/mat/image/Selection_009.png)
  - 图形标记(help gtext查询)
    - title(' ')
    - xlabel(' ')
    - ylabel(' ')
  - 设定坐标范围：axis([xmin,xmax,ymin,ymax])
  - 图例：legend('sin(x)','cos(x)')
- subplot(m,n,p)
  - <img src="/home/zpp/Documents/project/myml/mat/image/Selection_010.png" style="zoom:67%;" />

---

### 结构

- 条件
  - if cond1
    - xxx
  - elseif cond2
    - xxx
  - else
    - xxx
  - end

- swith
  - switch 表达式
  - case value1
    - xxx
  - case value2
    - xxx
  - ．．．
  - otherwise
    - xxx
  - end
- for　（循环语句会降低执行的速度）
  - for variable=初值：步长：终值
    - 循环体
  - end

- while
  - while cond
    - xxx
  - end

### 文件

- 命令文件
- 函数文件
  - 格式：
    - function [输出形参列表]＝函数名(输入形参列表)
      - 注释说明部分
      - 函数体
  - 例子
    - 函数文件examp.m
      - function fout=charray(a,b,c)
      - if nargin==1
        - fout=a;
      - else if nargin==2
        - fout=a+b;
      - else if nargin==3
        - fout=(a\*b\*c)/2
      - end
    - 命令文件mydemo.m
      - x=[1:3];
      - y=[1;2;3];
      - example(x)
      - example(x,y')
      - example(x,y,3)