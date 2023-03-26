# csdn2markdown
also known as [csdn to md] [csdn to markdown] [csdn 2 markdown]

language:[CN](#CN)/ [EN](#EN)

# CN

## 介绍

![iShot_2023-03-26_21.00.23](./assets/iShot_2023-03-26_21.00.23.png)

该仓库提供了一个shell脚本文件和一个python tkinter gui，可以将CSDN的博客导出为Typora格式的markdown文件。它支持单篇或整个专栏所有文章的导出操作，并且可以将本次所有导出内容汇总在一起变成一篇文章。

![iShot_2023-03-26_21.02.44](./assets/iShot_2023-03-26_21.02.44-9838730.png)



## 如何配置和使用

### 1, 安装python需求文档

该文件夹内运行终端，或者cd 到该文件夹下

```
pip install -r requirements.txt
```



### 2，配置aria2，pandoc，git

一切都在[support_files](./support_files)文件夹下, 查看该文件夹下的[README](./support_files/README.md)来获取更多信息



### 3,使用

如果使用shell，

双击`run.sh`即可使用，建议使用管理员模式。

也可以在该文件目录的cmd窗口输入 `sh run.sh` 使用。

如果使用gui，

双击`run.py`即可使用，建议使用管理员模式。

也可以在该文件目录的cmd窗口输入 `python run.py` 使用。



## 注意

有需要注意的地方：

- typora需要开启内联公式。
- 该转换仅针对typora格式，其他markdown编辑器可能会加载错误。



# EN



