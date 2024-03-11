from flask import Flask, render_template
from register import register_bp
from login import login_bp

app = Flask(__name__)

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

