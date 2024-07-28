from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen

def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))

boxen_print("tet this ",title="test", color="red")
class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("\n\n\n\n========= Sending messages ========= \n\n ")
        for message in messages[0]:
            if message.type == "system":
                boxen_print(message.content, title="system", color="yellow")

            elif message.type == "human":
                boxen_print(message.content, title="human", color="blue")

            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(f"running tool {call['name']}", title=message.type, color="cyan")

            elif message.type == "ai":
                boxen_print(message.content, title="ai", color="green")

            elif message.type == "function":
                boxen_print(message.content, title="ai", color="purple")


