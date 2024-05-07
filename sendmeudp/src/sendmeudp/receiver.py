import socket


class UDPReceiver:
    #def __enter__(self):
        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.sock.settimeout(self._timeout)
        #self.sock.bind(self._addr)

    def __exit__(self):
        self.sock.close()


    def __init__(self, host, port, timeout=60):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._addr = (self._host, self._port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(self._timeout)
        self.sock.bind(self._addr)

    def close(self):
        self.sock.close()

    def receive(self):
        return self.sock.recv(1).decode(encoding='utf-8')



