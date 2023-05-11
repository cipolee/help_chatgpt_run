import pdb
import socket
import openai
import os
import json
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
def get_openai_response(messages, max_tokens=2048):
    # 调用chatgpt
    print('>>>>>>>>>>>>print messages>>>>')
    print(messages)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    top_p=0,
    max_tokens=max_tokens,
    messages=messages
    )
    return completion
def run_server():
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定 socket 对象到主机名和端口号
        s.bind((HOST, PORT))
        i = 0
        while True:
            # 监听来自客户端的连接
            s.listen()
            print(f'server is listening on {HOST}:{PORT}')
            # 接受客户端的连接请求
            conn, addr = s.accept()
            print(f'connected by {addr}')
            # 接受客户端的发送数据，并进行解码
            client_data = conn.recv(2048).decode()
            # 使用json反序列化传输的数据
            messages = json.loads(client_data)
            # 请求chatgpt
            response = get_openai_response(messages)
            print(response)
            response_text = response.choices[0]['message']['content']
            # 向客户端发送消息
            conn.sendall(f'{response_text}'.encode())


            i += 1
            print(i)


if __name__ == '__main__':
    # 远程服务器的主机名和端口号
    HOST = 'x.x.x.x' # 主机ip
    PORT = 8888 # 端口号
    openai.api_key = '你的openai api_key'
    run_server()

