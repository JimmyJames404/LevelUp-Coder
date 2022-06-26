from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # This should be the name of your HTML file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismPercent = int(text1) + int(text2)
    if int(plagiarismPercent) == 50 :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>Vamos bien!</h1>"


@app.route('/test')
def suma():
    print("hello world")

if __name__ == '__main__':
    app.run()