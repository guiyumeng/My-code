#coding:utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) //使用IPV4通信地址，UDP传输协议
s.bind(('10.128.68.158',9999)) //10.128.68.158为服务器IP地址，9999为端口号
s.listen(1) //开始监听来自客户端的连接，只接受一个连接
print('Bind UDP on 9999...')
(conn,addr)=s.accept()
print('conn= ',conn)
print('addr= ',addr)
while True:
    str1=conn.recv(1024) //接受
    str2=str(str1,encoding='utf-8')
    print('I received a string is: ',str2)
    str3=str2.upper() //将字符串中的小写字母转化为大写字母
    conn.send(str3.encode('utf-8')) //发送回去
    if str2=='.':
        break
    conn.close()
    s.close()
