import os
import time
def write_line(path,text):
    with open(path,'a') as f:
        f.write(text+'\n')


if __name__ == '__main__':
    path = 'test.txt'
    inputed = input('请输入: ')
    write_line(path,inputed)