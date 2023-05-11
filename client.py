import socket
import json
# 远程服务器的主机名和端口号
HOST = 'x.x.x.x'  # 使用服务器的 IP 地址
PORT = 8888 #端口号


def run_client(Messages_INFO):
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到远程服务器
        s.connect((HOST, PORT))
        # 这里可以对Messages_INFO进行一些后处理
        messages = [
            {'system':'user','content':"""你的任务描述"""},
            {'role':'user','content':"""对话上下文"""},
        ]
        # 我这里messages和api需要的messages格式保持一致，因此传输的时候可以使用json进行序列化
        prompt = json.dumps(messages)
        # 编码成二进制，并发送
        s.sendall(prompt.encode())
        # 从服务器接收消息并解码
        data = s.recv(1024).decode()
        # 打印收到的消息并返回
        print('Received:', repr(data))
        return data


if __name__ == '__main__':
    Messages_INFO = "需要chatgpt处理的文本"
    run_client(Messages_INFO)

    
