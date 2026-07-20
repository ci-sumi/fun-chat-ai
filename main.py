import os
from dotenv import load_dotenv
# python talk to Groq's AI chat models.
from langchain_groq import ChatGroq

from flask import Flask

load_dotenv()
apikey=os.getenv('GROQ_API_KEY')
print(apikey)
model="llama-3.3-70b-versatile"
deepseek =ChatGroq(api_key=apikey,model=model)
print(deepseek.invoke("Hello, Tomi Tomi!"))
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h2>Hello, Tomi Tomi!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
