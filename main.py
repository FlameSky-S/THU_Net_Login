import argparse
import sys
from login import login
from logout import logout


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="清华大学准入代认证脚本")
        parser.add_argument('-m', '--mode', choices=['l', 'i', 'o', 'rl', 'ri'], required=True,
                            help="准入模式 l:校内认证; i:校外认证; o:注销; rl/ri:注销后再执行相应操作")
        parser.add_argument('-u', '--username', type=str, help="校园网账号")
        parser.add_argument('-p', '--password', type=str, help="校园网密码")
        parser.add_argument('--ac-id', type=str, default='159', help="不明参数, 仅供调试用, 默认值为159")
        args = parser.parse_args()
    except SystemExit as err: 
        if err.code == 2: 
            parser.print_help()
            sys.exit(0)

    if args.mode == 'l': # Local
        if args.username and args.password:
            res = login(args.username, args.password, False, args.ac_id)
            print(res)
        else:
            print("Username and password required.")
            parser.print_help()
            sys.exit(0)
    elif args.mode == 'i': # Internet
        if args.username and args.password:
            res = login(args.username, args.password, True, args.ac_id)
            print(res)
        else:
            print("Username and password required.")
            parser.print_help()
            sys.exit(0)
    elif args.mode == 'o': # Log off
        logout()
    elif args.mode == 'rl': # Relogin Local
        if args.username and args.password:
            logout()
            res = login(args.username, args.password, False, args.ac_id)
            print(res)
        else:
            print("Username and password required.")
            parser.print_help()
            sys.exit(0)
    elif args.mode == 'ri': #Relogin Internet
        if args.username and args.password:
            logout()
            res = login(args.username, args.password, True, args.ac_id)
            print(res)
        else:
            print("Username and password required.")
            parser.print_help()
            sys.exit(0)