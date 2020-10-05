from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: <richanshu.88@gmail.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print('Response of MAIL FROM')
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: <richanshu.88@gmail.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print('Response of RCPT TO')
    #print(recv3)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print('Response of DATA')
    #print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    #debugRECV = clientSocket.recv(1024).decode()
    #print("Response after sending message body")
    #print(debugRECV)
    quitCommand = 'QUIT \r\n'
    clientSocket.send(quitCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print('Response of QUIT')
    #print(recv5)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
