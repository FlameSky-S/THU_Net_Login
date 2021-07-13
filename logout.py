import requests

def logout():
    r = requests.get('http://auth4.tsinghua.edu.cn/cgi-bin/get_challenge?callback=jQuery&username=mhs20&ip=&double_stack=1&_=1625018780152')
    # print(r)

    r = requests.get('http://auth4.tsinghua.edu.cn/cgi-bin/srun_portal?callback=jQuery&action=logout&username=mhs20&ac_id=1&ip=&double_stack=1&info=%7BSRBX1%7DpbPdU1A9ViF0A3RRJ4tEE3d1Zlj4gfExYIzpCykccMBX25jdou4cbmqmYep0Ip10O4bttdZDopNgEmb6lNZGHv%3D%3D&chksum=879da958e56c36888e6928d3ecb9330c2ffee12f&n=200&type=1&_=1625018780153')
    # print(r)

