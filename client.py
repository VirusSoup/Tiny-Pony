# coding: utf-8
import socket

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHOST:127.0.0.1\r\n\r\n")

response = client.recv(4096)

print response