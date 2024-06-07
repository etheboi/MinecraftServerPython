class ReadChat:
    def __init__(self, connection):
        """
        Log the chat into a variable.
        Usage:
        chat_post = ReadChat(connection)
        if chat_post.message.startswith('!ping'):
            connection.send_message(f'player:{chat_post.author}', 'Pong!')
        """
        self.connection = connection
        self.connection.server.sendall("log\n".encode("utf-8"))
