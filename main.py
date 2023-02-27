import sys
import requests

url = "https://v1.hitokoto.cn/"

if __name__ == "__main__":
    print(sys.argv[1])
    rsp = requests.get(url)
    ret = rsp.json()
    print(ret["hitokoto"])