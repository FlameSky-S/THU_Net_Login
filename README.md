# 清华服务器校园网认证脚本

## 简介

通过 usereg 为服务器进行准入代认证时，经过若干时间（难以确定），服务器会自动断网。经测试，间歇性 ping 外网地址（ping -s 1500 -c 4 www.jd.com）无法解决断网问题。断网后再次准入代认证时，若使用不同校园网账号，无法正常登陆，须进入服务器图形界面将原校园网账号断开连接后才可正常联网。

为解决该问题，写了基于 python 的服务器自动断网联网脚本。校园网对于断网过程并无验证，所以使用固定请求即可。联网时，需要进行一系列的加密操作，这里一开始为了节省时间，直接利用`js2py`库调用 js 脚本中的加解密方式（xEncode 无 python 版，base64 与正常 base64 加密结果不同），但是加密结果是错误的（简单字符串加密经验证是正确的，但登陆时发送的 payload 加密结果是错误的，原因不明），经过一番痛苦的调试才定位到问题。最后感谢`huxiaofan1223`大佬提供的 python 版加密算法，省去了 js 转写 python 的麻烦。

## 使用方法

运行 `python relogin.py -u username -p password` 即可使服务器获取访问外网权限。

如仅需断网，执行 `python logout.py` 即可。
