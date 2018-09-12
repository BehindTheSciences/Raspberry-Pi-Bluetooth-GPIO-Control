import bluetooth 
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1 
server_sock.bind(("",port)) 
server_sock.listen(1) 
client_sock,address = server_sock.accept() 
print "Accepted connection from ",address 
while True: 
    recvdata = client_sock.recv(1024) 
    print "Received \"%s\" through Bluetooth" % recvdata 
    if (recvdata == "Q"): 
        print ("Exiting") 
        break 
        
client_sock.close() 
server_sock.close()
