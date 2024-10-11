from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        self.send({
            'type': 'websocket.accept',
        })
    
    def websocket_receive(self, event):
        print("rec. message",event)
        self.send({
            'type': 'websocket.send',
            'text': "Hello new message received",
        })
    
    def websocket_disconnect(self,event):
        self.send({
            'type': 'websocket.close',
        })
        print("disconnected")