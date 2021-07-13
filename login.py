import json
import re

import requests

from encode import *


def login(username, password, internet=True, ac_id='159'):
    username = username if internet else username + '@tsinghua'
    url_challenge = "http://auth4.tsinghua.edu.cn/cgi-bin/get_challenge"
    url_protal = "http://auth4.tsinghua.edu.cn/cgi-bin/srun_portal"
    payload = {'ac_id': ac_id, 'username': username, 'ip': '', 'double_stack': '1',
                'callback': 'jQuery'}
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

    r = requests.get(url=url_challenge, params=payload, headers=headers)
    data = json.loads(re.search('\{[^\}]+\}', r.text).group())

    token = data['challenge']
    # enc = "srun_bx1"
    n = 200
    _type = 1
    queryData = {}
    info_str = '{"username": "' + username + '", "password": "' + password + \
               '", "ip": "", "acid": "' + ac_id + '", "enc_ver": "srun_bx1"}'
    queryData['info'] = '{SRBX1}' + get_base64(get_xencode(info_str, token))
    hmd5 = get_md5(token, 'Wasd1234')
    queryData['password'] = "{MD5}" + hmd5
    chksum_str = token + username + token + hmd5 + token + ac_id + token + "" + \
                 token + str(n) + token + str(_type) + token + queryData['info']
    queryData['chksum'] = get_sha1(chksum_str)
    queryData['n'] = n
    queryData['type'] = _type
    queryData['callback'] = 'jQuery'
    queryData['action'] = 'login'
    queryData['username'] = username
    queryData['ac_id'] = ac_id
    queryData['ip'] = ''
    queryData['double_stack'] = '1'

    res = requests.get(url=url_protal, params=queryData)
    res = json.loads(re.search('\{[^\}]+\}', res.text).group())
    # print(res)
    if res['error'] == 'ok':
        return 'Login Successful'
    else:
        return res['error_msg']
