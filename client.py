import socket
import json
# 远程服务器的主机名和端口号
import time

HOST = 'x.x.x.x'  # 使用服务器的 IP 地址
PORT = 8888


def run_client(Messages_INFO):
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到远程服务器
        s.connect((HOST, PORT))
        # 可以使用Messages_INFO
        messages = [
            {'system':'user','content':"""你的任务描述"""},
            {'role':'user','content':"""对话上下文"""},
        ]
        ### 如果server端解析client端数据出现问题,则client再发送一次数据，直至没有问题
        ### 可能是socket的包缓存以及数据丢失导致server端无法解析client端发送的数据
        while True:
            # 我messages这里和api需要的messages格式保持一致，因此传输的时候进行json序列化
            prompt = json.dumps(messages)
            # 编码成二进制，并发送
            s.sendall(prompt.encode())
            # 从服务器接收消息
            data = s.recv(1024).decode()
            # 打印收到的消息
            print('Received:', repr(data))
            if data != 'transmission error':
                break
            time.sleep(1)
        return data


if __name__ == '__main__':
    Messages_INFO = "需要chatgpt处理的文本"
    run_client()

    
