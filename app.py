from flask import Flask, render_template, request
import google.generativeai as ai

app = Flask(__name__)

# Configure the AI model
API_KEY = 'AIzaSyBjyabyOHT1GKxwh2K-VXXlJ-w2IZJc1ms'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    if user_message.lower() == 'bye':
        return "Goodbye!"
    response = chat.send_message(user_message)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
