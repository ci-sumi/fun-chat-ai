import os
from dotenv import load_dotenv
# python talk to NVIDIA's AI chat models.
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()
apikey=os.getenv('NVIDIA_API_KEY')
model="nvidia/nemotron-3-super-120b-a12b"
deepseek = ChatNVIDIA(api_key=apikey, model=model)
print(deepseek.invoke("Hello, Tomi Tomi!"))