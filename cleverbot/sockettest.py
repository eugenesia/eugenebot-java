import socket, time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.listen(5000)
while 1:
    time.sleep(5) # wait 5 secs.
    data = client_socket.recv(512)
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print("RECIEVED:" , data)
        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data != 'Q' and data != 'q'):
            client_socket.send(data)
        else:
            client_socket.send(data)
            client_socket.close()
            break;

