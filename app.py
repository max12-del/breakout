from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'BOT STUMBIN™ ONLINE 🔥'

@app.route('/breakout-signal', methods=['POST'])
def breakout_signal():
    data = request.json
    message = data['message']
    print(f"Signal: {message}")
    return 'Breakout Signal Received!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
