# 行者历史数据批量导出

后续不会继续更新了 因为我已经全部导出迁移到garmin connect 上了

起因是心率带连接时跑步无法持续获取数据

为了不抛弃这将近10年的骑行历史数据,只能狠心导出迁移了


添了245, 加上心率带 做一名严肃跑者.


由于主要业余运动还是骑行所以之后还得更新下码表.

做这么多还不是因为两年没怎么运动胖了......



### 前置准备

- python 安装 selenium 并安装 chromedriver

以下说明均在 ***mac*** 中操作的记录. 


- 安装selenium 

    `$ pip install selenium`

- 下载chromedriver 

    需要选择于你电脑chrome相同版本的 driver使用

    https://chromedriver.chromium.org/downloads

- 将driver 放入到 /usr/local/bin 
    解压后
    `$ cp chromedriver /usr/local/bin`


以上为前置准备

使用selenium 原因为导出数据是弹出框下载,而非api数据返回,比较不才, 没有找到比较优雅的手段获取.
只能用这种比较暴力方法执行


### 执行流程





1. 使用 get_month_info 获取公共接口中每月的记录id并写入导出数据

    ```
    查找 user_id ,
    具体获取方法,登陆web
    在开发模式下查看 https://www.imxingzhe.com/api/v4/user_month_info 请求后的面的user_id 
    ```

    修改代码中 user_id = xxxx 为个人id信息
    

    `$ python get_month_info.py`

2. 获取cookies 用于临时登陆

    `$python get_cookies.py`

    启动界面后手动登陆账户等待退出 保存cookies 信息到本地

3. 下载历史记录

    ```
    打开 get_info.py  path 中添加需要保存文件的绝对路径 
    例如:
    path = '/Users/xxxx/github/xinzhe/download'
    ```

    `$python get_info.py`

4. 修改header 解决无法倒入到garmin connect 问题
    
    需要修改rootPath为上面path 相同的路径

    `$python modify_header.py`

修复问题参考来源: https://zhuanlan.zhihu.com/p/368952941
感谢原文作者




