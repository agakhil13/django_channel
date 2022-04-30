#Topic -- Consumer

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected',event)
        self.send({
            'type': 'websocket.accept'
        }
        )
    
    def websocket_receive(self, event):
        print("Message is: " + event['text'])
        self.send({
            'type': 'websocket.send',
            'text': 'Thankyou for Message'
        })
    def websocket_disconnect(self, event):
        print('websocket disconnected', event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connected', event)
        await self.send({
            'type': 'websocket.accept'
        }
        )
    
    async def websocket_receive(self, event):
        print('message received...', event)
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected', event)
        raise StopConsumer()