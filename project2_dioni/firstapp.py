from flask import Flask

firstapp = Flask(__name__)

@firstapp.route('/stuff')

def stuff():
    return "Hi Danil, Text is written here"

if __name__== '__main__':
    firstapp.run(host='localhost', port=5000)