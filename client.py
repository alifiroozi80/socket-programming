import socket

# ----------------- CONSTANT -----------------
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.1.6" # Work if acer is server
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

# ----------------- CLIENT SETUP -----------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# ----------------- START CLIENT SIDE -----------------


def send(msg: str):
    """
    This function is responsible for sending messages to the server and receive the server response.
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# ----------------- MESSAGES -----------------
send("Hello World!")
input()
send("Hello EveryOne!")
input()
send("Hello Ali!")
input()
send(DISCONNECT_MESSAGE)
