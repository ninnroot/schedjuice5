import asyncio
import json

from asgiref.sync import AsyncToSync, async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from .models import TestChannel


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "lobby"
        self.room_group_name = "test_lobby"
        async_to_sync(
            self.channel_layer.group_add(self.room_group_name, self.channel_name)
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "test_call_from_another",
                "message": "hello",
                "username": "username",
            },
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.channel_layer.send(text_data=json.dumps({"message": "hello world"}))
