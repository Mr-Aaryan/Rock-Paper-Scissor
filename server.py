import socket

def play_game(player1_move, player2_move):
    if(player1_move == '1' and player2_move == '2'):
        result = "Player2 wins"
    elif(player1_move =='1' and player2_move == '3'):
        result = "Player1 wins"
    elif(player1_move =='2' and player2_move == '1'):
        result = "Player1 wins"
    elif(player1_move =='2' and player2_move == '3'):
        result = "Player2 wins"
    elif(player1_move =='3' and player2_move == '1'):
        result = "Player2 wins"
    elif(player1_move =='3' and player2_move == '2'):
        result = "Player1 wins"
    else:
        result = "The game is draw."
    return result

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "192.168.1.97"                           #the above line gives this ipv4 address
ADDR = (SERVER, PORT)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(1)

    print("waiting for player2...")
    conn, addr = server_socket.accept()
    print("connected successfully")

    while True:
        player1_move = input("\n1.Rock\t2.Paper\t3.Scissor: ")
        conn.send(player1_move.encode())

        player2_move = conn.recv(1024).decode()
        print(f"\nPlayer2 move is {player2_move}\n")

        result = str(play_game(player1_move, player2_move))
        print(f"{result}\n")
        conn.send(result.encode())
        # print(conn.getpeername())
        play_again = input("Do you want to play again? (yes/no): ")
        conn.send(play_again.encode())
        try:
            if play_again.lower() != 'yes':
                break
            else:
                play_again_recv = conn.recv(1024).decode()
                if play_again_recv != 'yes':
                    print("Player2 is offline")
                    break
        except:
            print("Player2 is offline")
            exit()
            

        
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()    