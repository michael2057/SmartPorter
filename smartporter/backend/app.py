from flask import Flask, request, jsonify
import openai  
import os
from dotenv import load_dotenv
from flask_cors import CORS

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/chat', methods=['POST'])
def chat():
    if request.json is None:
        return jsonify({'error': 'Missing JSON request'}), 400
    message = request.json.get('message')
    if message is None:
        return jsonify({'error': 'Missing message in request'}), 400
    chatlog = request.json.get('chatlog', [])
    # chatlog.append({'role': 'system', 'content': '你是电脑小助手，一个帮助用户回答问题的人工智能'})
    chatlog.append({'role': 'user', 'content': message})
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=chatlog
    )

    print("chatlog=====>>"+response['choices'][0]['message']['content'])
    chatlog.append({'role': 'assistant', 'content': response['choices'][0]['message']['content']})

    
    return jsonify({'chatlog': chatlog}), 200

if __name__ == '__main__':
    app.run(debug=True)
