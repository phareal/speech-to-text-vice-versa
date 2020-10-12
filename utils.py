import socket

REMOTE_SERVER = "google.com"


def is_connected():
    try:
        host = socket.gethostbyname("google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False
