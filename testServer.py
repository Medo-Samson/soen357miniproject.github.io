from socket import *

servSock = socket(AF_INET, SOCK_STREAM)
servSock.bind(("127.0.0.1", 80))
servSock.listen(1)
print('server listening...')

while True:
    cliSock, ipAddr = servSock.accept()
    print('\nnew connection:', ipAddr)
    
    lines = cliSock.recv(1024).decode().split('\n')
    line1 = lines[0].split(' ')
    print('req:\n' + ' '.join(line1))
    
    if line1[0] == 'GET':
        data = ''
        if line1[1] == '/':
            header = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
            data = 'Hello world!'
        else:
            header = 'HTTP/1.1 404 Not Found\n\n'
        
        response = header + data
        print('\nsending response:\n' + response)
        cliSock.send(response.encode())
    
    cliSock.close()
    print('\nconnection closed')