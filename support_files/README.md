# What you need

## aria2

- put the folder [aria2](./aria2) to the places you want, like c:\ ,then add the folder path in to your system user variant - Path.
- Adjust the file path in [aria2.conf](aria2.conf), the line you need to adjust is marked in ###, dir is the path of the download file, other is the path of log file and  session file in this  folder

```
dir=C:\Users\tlpa\Downloads\ ###

log=D:\aria2\Aria2.log  ###

input-file=D:\aria2\aria2.session ###

save-session=D:\aria2\aria2.session ###
```

- for more of aria2, check [this markdown file](Aria2_安装和使用全教程.md) in Chinese



you may want to know

Use:

    运行 aria2.exe
    访问 http://aria2c.com/ 查看状态

file declaration:

    aria2.conf    # 配置文件 可以自己根据说明修改
    aria2.exe     # 启动文件 使用这个来启动 aria2
    aria2.session # 任务保存文件 未完成任务会保存在这里
    aria2c.exe    # 命令行主程序
    README.md     # README





## pandoc

go to [this web page](https://pandoc.org/installing.html), download the sufficient pandoc install pack and install it



## Git

go to [this page](https://git-scm.com/), download the sufficient git install pack and install it