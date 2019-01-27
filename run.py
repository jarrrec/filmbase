from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
 return 'Hello to the World of Flask!'

@app.route('/pozdrav')
def pozdrav():
 return 'Pozdravujem!'

if __name__ == '__main__':
 #Load this config object for development mode
 app.config.from_object('configurations.DevelopmentConfig')
 app.run()