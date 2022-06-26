import profile
from flask import Flask
from flask import request
from flask import render_template
import weights


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # This should be the name of your HTML file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']
    text4 = request.form['text4']
    text5 = request.form['text5']
    
    
    profile = { 
            'name' : text1,
            'email': text2,
            'stack_overflow': text3,
            'github': text4,
            'leetcode': text5
            }
    
    if text1 != 50 :
        
        return procesor(profile)
    else :
        return "<h1>Vamos bien!</h1>"
    
def procesor(profile):
    stack_link = profile['stack_overflow']
    github_name = profile['github']
    leet_name = profile['leetcode']
    rank = weights.rank(stack_link, github_name, leet_name)
    print(rank)
    
    return "flash('You were successfully registered {}')".format(rank)
    #return "<h1>Te enviamos un mensaje a tyu correo!{}</h1>".format(rank)

if __name__ == '__main__':
    app.run()
    
    
    # Me dio hambre yy me puse a preparar quesadillas
    