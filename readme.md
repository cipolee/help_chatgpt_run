# 基于socket通信的chatgpt使用方法
## Overview
事件起因：想探索一下对话阅读理解任务中调用chatgpt和问答模型交互，用来评估问答模型的回复能力，但是很快遇到一个问题: 问答模型放在学校服务器上，而学校服务器上不能直接调用chatgpt的api。


因此如果实现通过服务器到本机的通信，既可以实现服务器调用chatgpt api。

服务器到本地的通信可以基于**socket**实现， 实现通信需要两个文件，client.py和server.py. server.py放在本地用来启动服务，client.py放在服务器，在需要访问chatgpt时调用
client.py的函数run_client(prompt)。




![Socket通信模型](assets/socket通信模型.jpg)
<center>Socket通信模型</center>

**Update 2024.2.28：为了保护服务器，学校把GPU节点与网络隔绝开，任何端口都路由不到。不过还好GPU节点和管理节点文件系统上是共享的，于是通过读写文件进行共享**

* 实现坑点
  * 与本地修改Command+S不同，使用watchdog监控文件不能监控GPU节点的程序读写，可能程序写入存在缓冲区，本地节点其他程序写入在打开文件和写入文件时会各修改文件一次。
  * 监控的原理均是每隔一段时间运行检测函数，因此不存在时间复杂度低的算法，可本地实现无限循环的读取比对函数。
* 文件对应
  * local_node： 本地节点运行，负责检测文件写入，并交给ChatGPT处理
  * gpu_node: 显卡节点负责使用A100运行大模型

## Quick start
1. 确保本地可以访问chatgpt
2. 查看本地ip
```shell
# Windows 查看方法命令行输入
ipconfig
# Linux 查看ip方法
ip address
```
3. 
  1. 将第2步得到的ip写入server.py和client.py
  2. 本地运行server.py
  3. 在服务器需要调用chatgpt的py文件里from client import run_client,通过调用run_client(prompt)来使用chatgpt


## 相关知识
[network socket](https://en.wikipedia.org/wiki/Network_socket)

[socket 教程](https://realpython.com/python-sockets/)

[socket编程 中文博客](https://blog.csdn.net/Dustinthewine/article/details/127631711)