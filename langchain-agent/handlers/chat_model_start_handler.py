from typing import Dict, Any, List, Optional
from uuid import UUID

from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import ChatMessage, BaseMessage


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print(messages)

