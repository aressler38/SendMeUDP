import asyncio
from sendmeudp import receiver
from sendmeudp import sender


async def test_sender():
    with receiver.UDPReceiver("127.0.0.1", 5757) as srv:
        with sender.UDPSender("127.0.0.1", 5757) as cli:
            pass
