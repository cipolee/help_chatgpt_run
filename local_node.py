import time
from client import run_client
def check_diff(pre):
    with open('./test.txt', 'r') as file:
        lines = file.readlines()
        last_line = lines[-1]
        if last_line != pre:
            run_client(last_line)
            pre = last_line
    return pre
if __name__ == "__main__":
    path = "./test.txt"  # 监控当前目录下的文件，可根据实际情况更改路径
    with open('./test.txt', 'r') as file:
        lines = file.readlines()
        pre = lines[-1]
    try:
        while True:
            pre = check_diff(pre)
            time.sleep(1)
    except KeyboardInterrupt:
        print('stop')
