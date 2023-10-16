from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)

def make_bold(fn):
    def wrapper(*args, **kwargs):
        return f"<b>{fn(**kwargs)}</b>"
    
    return wrapper

@app.route('/') 
def hello():
    global number
    number = random.randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1> \
        <img src='https://media4.giphy.com/media/MAuWs1rqbfHFMWUCYH/giphy.gif?cid=ecf05e47ruy3esxoburv8darc8qgn11fzceeiaey4g9c6tbv&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g' \>"

@app.route('/user/<string:username>')
@make_bold
def hi(*args, **kwargs):
    return f"Hi {kwargs['username']}"

@app.route('/<int:guessed_number>')
def guess(guessed_number):
    if guessed_number < number:
        return f"<h2 style='color:red'>Too low, try again!</h2>\
            <img src='https://media3.giphy.com/media/13xHqoOQOdFu5a/giphy.gif?cid=ecf05e47vut817wv23uh4kv0kn1u1dr9ejmg0ixdq8vfy6ly&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g' \>"
    elif guessed_number > number:
        return f"<h2 style='color:purple'>Too high, try again!</h2>\
            <img src='https://media0.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy.gif?cid=ecf05e47ceamxo6d50ps5ysyuswwg8r8y1j5ghpi0egfxb8p&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g' \>"
    else:
        return f"<h2 style='color:green'>You found me!</h2>\
            <img src='https://media1.giphy.com/media/cdNSp4L5vCU7aQrYnV/giphy.gif?cid=ecf05e47352q7binx9x8yeac7chezqmnj2i9pmqlj0sp70yz&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g' \>"

if __name__ == "__main__":
    app.run(debug=True)
