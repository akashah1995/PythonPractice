from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    try:
        session['compnum'] = session['compnum']

    except KeyError:
        session['compnum'] = random.randrange(0, 101)

    return render_template('greatnumbergame.html')


@app.route('/tryagain', methods = ['POST'])
def guess():
    guess = int(request.form['guess'])
    print guess
    if guess > session['compnum']:
        return render_template('toohigh.html')

    elif guess < session['compnum']:
        return render_template('toolow.html')

    else:
        return render_template('gotit.html')

@app.route('/restart', methods = ['POST'])
def restart():
    session.pop('compnum')
    return redirect('/')
    
app.run(debug=True)






