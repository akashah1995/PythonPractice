from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():

    try:
        session['counter'] += 1
    
    except KeyError:
        session['counter'] = 1
    

    return render_template("countdisplay.html")

@app.route('/reload', methods = ['POST'])
def reload():

    session['counter'] += 1

            
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():

    session['counter'] = 0

            
    return redirect('/')


app.run(debug=True)

