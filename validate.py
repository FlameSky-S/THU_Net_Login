from encode import get_md5
import hashlib
import requests

# def validate(username, password):
#     """
#     首先利用 id.tsinghua.edu.cn 验证账号密码，避免登陆失败导致服务器断网无法连接
#     """
#     url = "https://id.tsinghua.edu.cn/security_check"
#     payload = {'username': username, 'password': password}
#     # headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
#     r = requests.post(url, payload)
#     if '账号设置' in r.text:
#         return True
#     else:
#         return False


def validate(username, password):
    """
    首先利用 usesreg.tsinghua.edu.cn 验证账号密码，避免登陆失败导致服务器断网无法连接
    """
    url = "http://usereg.tsinghua.edu.cn/do.php"
    password = hashlib.md5(password.encode()).hexdigest()
    payload = {'action': 'login', 'user_login_name': username, 'user_password': password}
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.post(url, payload)
    if r.text == 'ok':
        return True
    else:
        return False
