import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8083))
serv.listen(1)
while True:
    conn, addr = serv.accept()
    print(conn, addr)
    from_client = ''
    while True:
        data = conn.recv(4096)

        print(data)
        if not data:
            print('sdfsfsf')
            break
        # from_client += data
        print(from_client)
        conn.send(b"I am SERVER<br>")
    conn.close()
    print('client disconnected')

# import socket
#
# HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
# PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(2)
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             print('daf')
#             data = conn.recv(1024)
#             if not data:
#                 print('without data')
#                 break
#             print(f'{data=}')
#             conn.sendall(data)