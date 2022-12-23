import argparse
import subprocess

from login import login
from logout import logout


def ping(host):
    command = ['ping', '-c', '1', host]
    return subprocess.call(command) == 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="清华大学准入代认证脚本")
    parser.add_argument('-u', '--username', type=str, help="校园网账号")
    parser.add_argument('-p', '--password', type=str, help="校园网密码")
    args = parser.parse_args()

    res = ping('its.tsinghua.edu.cn')
    # print(res)
    if not res:
        logout()
        res = login(args.username, args.password, False)
