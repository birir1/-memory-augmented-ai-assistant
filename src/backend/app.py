from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp
from routes.memory_routes import memory_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)
app.register_blueprint(memory_bp)

if __name__ == "__main__":
    app.run(debug=True)
