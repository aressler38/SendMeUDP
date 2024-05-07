import socket


class UDPSender:
    def __enter__(self):
        pass

    def __exit__(self):
        self.sock.close()


    def __init__(self, host, port, timeout=60):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._addr = (self._host, self._port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
        self.sock.settimeout(self._timeout)
        self.sock.connect(self._addr)

    def send(self, text:str):
        #self.sock.bind(self._addr)
        result = self.sock.send(text.encode('utf-8'))
        return result



