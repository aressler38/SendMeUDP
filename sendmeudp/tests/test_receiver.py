import asyncio
from sendmeudp import receiver
from sendmeudp import sender


def test_receiver():
    srv = receiver.UDPReceiver("127.0.0.1", 5758)
    data = srv.receive()
    srv.close()
    print("\nGotData %s" % data)
    assert data == "X"


