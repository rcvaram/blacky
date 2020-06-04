import socket

# Assumptions that we made here are
# 1.Always connection should be succeed
# 2.Always server is expecting to data from client first
target_host = "0.0.0.0"
target_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# send some data
client.send("hi".encode())

# receive some data
response = client.recv(1024)

print(response.decode())
