import socket
import threading

ip_addr = "0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip_addr, port))

server.listen(5)

print("[-] Listnening on {}:{}".format(ip_addr, port))


def handle_client(client_socket):
  req = client_socket.recv(1024)
  print("[-] Received Data --> {}".format(req.decode()))
  client_socket.send("ACK!".encode())
  client_socket.close()


while True:
  client, addr = server.accept()
  print("[-] Connection Accepted From {}:{}".format(addr[0], addr[1]))
  client_handler = threading.Thread(target=handle_client, args=(client,))
  client_handler.start()
