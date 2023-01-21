from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = 'smtp.csus.edu'
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <hetviapatel@csus.edu>\r\n'
clientSocket.send(mailFrom)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = 'RCPT TO: <hetvip2602@gmail.com>\r\n'
clientSocket.send(rcptto)
recv3 = clientSocket.recv(1024)
print(recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
print(recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send('SUBJECT: Hello to you! Have a nice day:)\r\n')
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print(recv5)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcommand = 'QUIT\r\n'.encode()
clientSocket.send(quitcommand)
recv6 = clientSocket.recv(1024)
print(recv6)

clientSocket.close()
# Fill in end


