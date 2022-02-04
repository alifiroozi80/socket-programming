import socket
import threading

# ----------------- CONSTANT -----------------
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# ----------------- SERVER SETUP -----------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# ----------------- FUNCTIONS -----------------


def handle_client(conn, addr):
    """
    This function is responsible for handle client side.
    """
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received!".encode(FORMAT))

    conn.close()


def start():
    """
    This function is just simply responsible for render our server.
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")


# ----------------- START SERVERE -----------------
print(f"[STARTING] Server is up and running on port {PORT}")
start()
