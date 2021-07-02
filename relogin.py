from login import login, parse_args
from logout import logout

if __name__ == '__main__':
    args = parse_args()
    logout()
    login(args.username, args.password, args.ac_id)