import socket
import sys
from cbot_browser import chat

CHUNK_SIZE = 16
CONNECTIONS_COUNT = 5
LISTEN_PORT = 10000
LISTEN_HOST = 'localhost'

def remove_non_words(string):
  split = string.split()
  return ' '.join(split)

def receive_message(connection):
  data = b'' # Initialise byte string
  while True:
    try:
      # Receive the data in small chunks
      chunk = connection.recv(CHUNK_SIZE)
    except Exception as e:
      print(e, file=sys.stderr, flush=True)
      break

    print(f"Received '{chunk}'", file=sys.stderr, flush=True)
    if chunk:
      data += chunk
      # A message usually ends in a newline
      # If received chunk is less than max size, we've reached the end of message
      if len(chunk) < CHUNK_SIZE and b'\n' in chunk:
        print(f"End of message. Chunk size {len(chunk)}", file=sys.stderr, flush=True)
        break
    else:
      print("No more chunks", file=sys.stderr, flush=True)
      break
  
  message = data.decode(errors='ignore')
  return message

def cleanup(sock, connection):
  connection.close() # Clean up the connection
  sock.close()


if __name__ == '__main__':

  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Bind the socket to the port
  server_address = (LISTEN_HOST, LISTEN_PORT)
  print(f"Starting up on {server_address}", file=sys.stderr, flush=True)
  sock.bind(server_address)

  # Listen for incoming connections
  sock.listen(CONNECTIONS_COUNT)

  # Loop to handle new connections
  while True:
    # Wait for a connection
    print("Waiting for a connection", file=sys.stderr, flush=True)
    connection, client_address = sock.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]}", file=sys.stderr, flush=True)

    try:
      # Loop with the same connection to handle multiple incoming messages
      while True:
        message = receive_message(connection)
        message = remove_non_words(message) # Remove <SOME-SLACK-ID> which Cleverbot doesn't need

        print(f"Sending message '{message}' to Cleverbot", file=sys.stderr, flush=True)
        resp = chat(message) + "\n"
        resp_bytes = resp.encode()

        try:
          print(f"Sending response back to the client: '{resp}'", file=sys.stderr, flush=True)
          connection.sendall(resp_bytes)
        except Exception as e:
          print(f"Error on sending response back to client: {e}", file=sys.stderr, flush=True)
          break # Client may have terminated, wait for a new connection

    finally:
      connection.close()
