import requests

def validate(username, password):
    """
    首先利用id.tsinghua.edu.cn验证账号密码，避免登陆失败导致服务器断网无法连接
    """
    url = "https://id.tsinghua.edu.cn/security_check"
    payload = {'username': username, 'password': password}
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.post(url, payload)
    if '账号设置' in r.text:
        return True
    else:
        return False