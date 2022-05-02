#Topic -- Consumer

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected',event)
        self.send({
            'type': 'websocket.accept'
        })
    
    # def websocket_receive(self, event):
    #     print("Message is: " + event['text'])
    #     for i in range(10):
    #         self.send({
    #         'type': 'websocket.send',
    #         'text': str(i)
    #         })
    #         sleep(1)
    def websocket_receive(self, event):
        print("Message is: " + event['text'])
        for i in range(10):
            self.send({
            'type': 'websocket.send',
            'text': json.dumps({'count': i})
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print('websocket disconnected', event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connected', event)
        await self.send({
            'type': 'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print('message received...', event['text'])
        for i in range(10):
            await self.send({
            'type': 'websocket.send',
            'text': str(i)
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected', event)
        raise StopConsumer()