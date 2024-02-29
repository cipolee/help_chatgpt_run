import socket
import json
import time
# HOST = '127.0.0.1'  # 或者使用远程服务器的 IP 地址
HOST = '10.10.64.165'
PORT = 8888
def run_client(question):
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到远程服务器
        s.connect((HOST, PORT))
        messages = [
            {'role':'system','content':"""you ara a assistant, help user in question answering"""},
            {'role':'user','content':question}
        ]


        while True:
            # 我messages这里和api需要的messages格式保持一致，因此传输的时候进行json序列化
            prompt = json.dumps(messages)
            # 编码成二进制，并发送
            print(prompt)
            s.sendall(prompt.encode())
            print('已发送')
            # 从服务器接收消息
            data = s.recv(1024).decode()
            # 打印收到的消息
            print('Received:', repr(data))
            if data!='transmission error':
                break
            time.sleep(0.5)
    return data


if __name__ == '__main__':

    run_client('1+1')