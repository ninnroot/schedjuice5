import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "lobby"
        self.room_group_name = "test_lobby"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        td_json = json.loads(text_data)
        message = td_json["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": td_json["username"],
            },
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps({**event}))
