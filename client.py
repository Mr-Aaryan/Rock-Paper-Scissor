import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.1.97", 5050)
    client_socket.connect(addr)

    while True:
        player2_move = input("\n1.Rock\t2.Paper\t3.Scissor: ")
        client_socket.send(player2_move.encode())

        player1_move = client_socket.recv(1024).decode()
        print(f"\nPlayer1 move is {player1_move}\n")

        result = client_socket.recv(1024).decode()
        print(f"{result}\n")

        play_again = input("Do you want to play again? (yes/no): ")
        client_socket.send(play_again.encode())
        try:
            if play_again.lower() != 'yes':
                break
            else:
                play_again_recv = client_socket.recv(1024).decode()
                if play_again_recv != 'yes':
                    print("Player1 is offline")
                    break
        except:
            print("Player1 is offline")
            exit()

    client_socket.close()

if __name__ == "__main__":
    start_client()
