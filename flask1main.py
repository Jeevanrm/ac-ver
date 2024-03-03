from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World this is from docker'
@app.route('/name')
def hello_name():
   return 'my name is thippesh'
if __name__ == '__main__':
   app.run()
