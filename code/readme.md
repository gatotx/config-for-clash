# 使用环境

`python 3.0`

需额外安装的库：`requests`

# 文件介绍

## log 文件夹

存放日志文件

每成功运行一次`_main.py`都将生成一个日志文件

内容包括：机场名字，对应的`url`，获得节点数量，生成的配置文件名称

### 内容示例：
```
airpot_name: erye
url: https://jiang.netlify.app/
node_nums: 110
config_file_name: test.yaml
```
## code 文件夹

存放代码文件


# 缺陷

3. 必须按照指定形式输入，没有异常处理机制

# 使用示例

运行`_main.py`

![image](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-08-38.jpg)

要生成多少配置文件就输入几

**若输入的数字为n，下面的步骤将重复n遍**

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-10-21.jpg)

若第一次运行`_main.py`则会出现如上提示

若输入**1**则将创建`archives.json`记录文件，以后可以直接从中读取url

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-10-40.jpg)

程序将在关键点输入日志，提醒用户

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-11-17.jpg)

将会记录用户的订阅信息

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-11-33.jpg)

在下载数据前会打印原有订阅信息

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-11-57.jpg)

选择对应的订阅信息下载数据

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-12-11.jpg)

是否为配置文件取名

若否将按运行程序时间起名

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-12-22.jpg)

是否启用dns、tun 模式

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-12-33.jpg)

这两个日志就代表成功生成配置文件，可在`_main.py`根目录下找到

若用户有多个文件生成则将重复以上步骤

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-27-38.jpg)

若已存在`archives.json`则运行程序时会首先输出如下信息,输入对应的数字可实现增、删、改

![picture](https://github.com/eastarpen/config-for-clash/blob/master/Picture/Snipaste_2021-04-12_19-29-45.jpg)

若选择不生成`archives.json`可按上图操作