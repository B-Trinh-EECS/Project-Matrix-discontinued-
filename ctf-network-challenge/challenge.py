import socket

HOST = "0.0.0.0"
PORT = 9001
FLAG = "falcon{using_netcat_seem_relatively_simple}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            conn.sendall(b"Welcome to the networking challenge! \n")
            conn.sendall(b"Find the secret... \n\n")
            conn.sendall(FLAG.encode() + b"\n")
