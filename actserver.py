import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Sunucu Online!")

while True:
    clientsocket, adress = s.accept()
    print(f"{adress} ile bağlantı kuruldu!")
    mesaj = clientsocket.recv(1024).decode("utf-8")
    print(mesaj)
    clientsocket.send(bytes(f"1", "utf-8"))
