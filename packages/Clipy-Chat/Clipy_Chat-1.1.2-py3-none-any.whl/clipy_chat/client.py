# clipy_chat/client.py

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred!")
            client_socket.close()
            break

def main():
    server_ip = input("Enter the server IP address: ")
    server_port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    room_id = input("Enter the room ID: ")
    client_socket.send(room_id.encode('utf-8'))
    client_socket.recv(1024).decode('utf-8')  # ROOM_ID prompt

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))
    client_socket.recv(1024).decode('utf-8')  # USERNAME prompt

    print(f"Connected to room: {room_id} as {username}")

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
