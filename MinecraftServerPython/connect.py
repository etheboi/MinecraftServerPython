import socket
import threading


class Connect:
    def __init__(self, server_address):
        """
        Connect to your Minecraft server!
        Usage: mc = Connect(("127.0.0.1", 12345))
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.connect(server_address)
            print("Connected to server!")
        except Exception as e:
            print(
                "Error connecting to server! Make sure that you have a Minecraft server running with the plugin installed.")
            print(e)
            exit()

    def send_message(self, player: str, message: str):
        """
        Send a message to players.
        Usage: mc.send_message("etheboi" OR "all_players", "Put what you want here --->&<--- THOSE WORK!")
        """
        if player == "all_players":
            self.server.sendall(f"say all_players {message}\n".encode("utf-8"))
        else:
            self.server.sendall(f"say player:{player} {message}\n".encode("utf-8"))

    def console_command(self, command: str):
        """
        Execute a command as the console.
        Usage: mc.console_command("give @a diamond_block 64")
        """
        self.server.sendall(f"execute console {command}\n".encode("utf-8"))

    def player_command(self, player: str, command: str):
        """
        Execute a command as a player.
        Usage: mc.player_command("etheboi", "give @s diamond_block 64")
        """
        self.server.sendall(f"execute player:{player} {command}\n".encode("utf-8"))

    def receive_messages(self):
        """
        Start receiving messages from the server.
        """

        def handle_receive():
            while True:
                try:
                    data = self.server.recv(1024).decode("utf-8")
                    if data:
                        print("Received:", data)
                    else:
                        break
                except Exception as e:
                    print("Error receiving data:", e)
                    break

        thread = threading.Thread(target=handle_receive)
        thread.start()

    def close(self):
        """
        Close the connection to the server.
        """
        self.server.close()
