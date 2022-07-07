from flask import Flask

app=Flask(__name__)

@app.route("/", methods = ['Get', 'POST'])

def index():
    return "Flask testing"

if __name__=='__main__':
    app.run(debug=True)
