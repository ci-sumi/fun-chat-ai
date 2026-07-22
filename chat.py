import os
from dotenv import load_dotenv
# python talk to NVIDIA's AI chat models.
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()
apikey=os.getenv('NVIDIA_API_KEY')
model="nvidia/nemotron-3-super-120b-a12b"
llm = ChatNVIDIA(api_key=apikey, model=model,temperature=0.7)
messages = [
    SystemMessage(content="You are a TomiBot.You are funny and friendly.")]

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Exiting the chat...")
        break
    else:
        messages.append(HumanMessage(content=user_input))
        response = llm.invoke(messages)
        messages.append(AIMessage(content=response.content))
        print("TomiBot:", response.content)