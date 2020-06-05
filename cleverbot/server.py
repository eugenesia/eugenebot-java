import socket
import sys
from cbot_browser import chat

def remove_non_words(string):
  split = string.split()
  return ' '.join(split)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

while True:
  # Wait for a connection
  print('waiting for a connection', file=sys.stderr)
  connection, client_address = sock.accept()
  print(connection)
  print(client_address)
  try:
    print('connection from ' + client_address[0] + ' ' + str(client_address[1]), file=sys.stderr)

    # Receive the data in small chunks and retransmit it
    while True:
      data = connection.recv(16)
      print('received "%s"' % data, file=sys.stderr)

      if data:
        trimmed_data = remove_non_words(data.decode('utf-8'))
        resp = chat(trimmed_data)
        resp_bytes = resp.encode()
        print('sending response back to the client %s' % resp, file=sys.stderr)
        connection.sendall(resp_bytes)
      else:
        print('no more data from ' + client_address, file=sys.stderr)
        break

  finally:
    # Clean up the connection
    connection.close()
