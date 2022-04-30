#Topic -- Consumer

from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected',event)
        self.send({
            'type': 'websocket.accept'
        }
        )
    
    def websocket_receive(self, event):
        print('message received...', event)
        print("Message is: " + event['text'])
    
    def websocket_disconnect(self, event):
        print('websocket disconnected', event)

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connected', event)
    
    async def websocket_receive(self, event):
        print('message received...', event)
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected', event)