# nenuschedulebattle

## 注意！
该项目停止维护，不再保证其正确性。

p.s. 如果想要抢课，其实只需要找到选课的post包，用Charles甚至curl开多线程就成了，就别这么麻烦了。

## 概述
本人以前写的一个抢课脚本，现在选修课很多了就不再用了，基本思路是用grequests库异步post多个课程的请求，如果想要更加精致可以爬取整理一份课程与对应编号的字典，直接输课程名字即可。想要继续开发的学弟学妹可以在这个粗糙的版本上改进。

## 用法
1、pip3 install -r requirements.txt

2、python3 NENU.py

3、输入账号和密码（账号是你邮箱@前的部分）

4、按照提示填写信息

其中课程号是课程名称前的那一串数字

注意看课堂名称后面有没有(2)
![image](https://github.com/zhangxm99/nenuschedulebattel/blob/master/pic.png)

输完记住敲回车

## 注意事项
1、url_show里面的jx0502zbid码每次会变，这个码可以在选课界面的网址栏里找到

2、server在本部和净月不一样，注意留意更改
