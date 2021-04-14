# 简介

本项目将解析`vmess`、`ss`、`trojan`订阅链接，并将其内容转换为`clash配置文件 config.yaml`

所有代码均为`python`

# 使用环境

`python 3.0`

需额外安装的库：`requests`

# 使用方法

打开![image](https://github.com/eastarpen/config-for-clash/blob/master/Picture/image-20210412184039515.png)并运行
按提示输入相关信息即可

# 文件介绍

## log 文件夹

存放日志文件

每成功运行一次`_main.py`都将生成一个日志文件

内容包括：机场名字，对应的url，获得节点数量，生成的配置文件名称

### 内容示例：
```
airpot_name: erye
url: https://jiang.netlify.app/
node_nums: 110
config_file_name: test.yaml
```
## code 文件夹

存放代码文件


# 问题

1. 示例订阅地址必须关闭代理才能下载
2. 有些地址开代理无法下载
3. 必须按照指定形式输入，没有异常处理机制

# TODO

1. vless,和ssr的解析
2. 完善异常设计
3. 解决下载问题
4. 打包为exe文件
5. 可视化开发

# 其他

本项目附带@ugvf2009的[Miles](https://github.com/ugvf2009/Miles)收集的免费订阅地址

配置文件中rule-providers复制自@Loyalsoldier的[clash-rules](https://github.com/Loyalsoldier/clash-rules)项目
