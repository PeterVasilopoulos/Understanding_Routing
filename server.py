from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hi(name):
    if isinstance(name, str):
        return f"Hello {name}!"
    else:
        return "Please provide a name"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    str = ""
    try:  
        num = int(num)
    except:
        return "Please provide a number and a word"

    # if isinstance(num, int) and isinstance(word, str):
    #     for i in range(int(num)):
    #         str += f"{word}\n"
    #     return str
    # else:
    #     return "Please provide correct values"

    for i in range(num):
        str += f"{word}\n"
    return str

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug = True)