1. 使用 get_month_info 获取公共接口中每月的记录id并写入导出数据
$python get_month_info.py

2. 获取cookies 用于临时登陆

$python get_cookies.py

启动界面后手动登陆账户等待退出 保存cookies 信息到本地

3. 下载历史记录

$python get_info.py


4. 修改header 解决无法倒入到garmin connect 问题

$python modify_header.py

修复问题参考来源: https://zhuanlan.zhihu.com/p/368952941
感谢原文作者
