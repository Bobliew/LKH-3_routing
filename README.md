# LKH-3的Python封装
## 思路
根据 [LKH-3官方](http://webhotel4.ruc.dk/~keld/research/LKH-3/)提供的二进制文件，进行了Python封装，处理方式还是对本地文件进行读写，该方法存在的缺陷在并发环境下存在数据竞争的问题，目前的处理方案比较取巧，就是通过生成不同名称的数据集，来避免数据竞争问题。后续将考虑对LKH-3源码进行研究，尝试找到根源上的解决方案。
## 使用方法
参见[此处](https://github.com/Bobliew/LKH-3_routing/blob/main/Lkh/lkh_test.py)
## Other
有任何问题，可以提出Issues，如果可以的话给个星星吧！
