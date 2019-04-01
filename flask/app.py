from flask import Flask
app = Flask(__name__)
app.config['ENV']= 'development'
@app.route('/')
def hello():
    return "hello docker"
if __name__ == '__main__':
    app.run()
