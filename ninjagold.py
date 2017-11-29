from flask import Flask, render_template, request, redirect, session
import random
import time

REGEX_Uppercase: 

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

app = Flask(__name__)
app.secret_key = 'ThisIskindasecret'
@app.route('/')
def index():
    try:
        session['totalgold'] = session['totalgold']

    except KeyError:
        session['totalgold'] = 0
    try:
        session['activ'] = session['activ']
    except:
        session['activ'] = list()
    
    try:
        session['size'] = session['size']

    except KeyError:
        session['size'] = 0
    
    try:
        session['x'] = session['x']

    except KeyError:
        session['x'] = 0

    return render_template('ninjagold.html')



@app.route('/farm', methods = ['POST'])
def farm():
    print "hi"
    session['x'] = random.randint(10,20)
    session['totalgold'] += session['x']
    localtime = time.asctime( time.localtime(time.time()) )
    session['activ'].append("Earned " + str(session['x']) + " golds from the farm! " + str(localtime))
    session['size']= len(session['activ'])
    print session['size']
    return redirect('/')

@app.route('/cave', methods = ['POST'])
def cave():
    session['x'] = random.randint(5,10)
    session['totalgold'] += session['x']
    localtime = time.asctime( time.localtime(time.time()) )
    session['activ'].append("Earned " + str(session['x']) + " golds from the cave! " + str(localtime))
    session['size']= len(session['activ'])
    print session['size']
    return redirect('/')

@app.route('/house', methods = ['POST'])
def house():
    session['x'] = random.randint(2,5)
    session['totalgold'] += session['x']
    localtime = time.asctime( time.localtime(time.time()) )
    session['activ'].append("Earned " + str(session['x']) + " golds from the house! " + str(localtime))
    session['size']= len(session['activ'])
    print session['size']
    return redirect('/')

@app.route('/casino', methods = ['POST'])
def casino():
    session['x'] = random.randint(-50,50)
    session['totalgold'] += session['x']
    localtime = time.asctime( time.localtime(time.time()) )
    session['activ'].append("Earned " + str(session['x']) + " golds from the casino! " + str(localtime))
    session['size']= len(session['activ'])
    print session['size']
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session['totalgold'] = 0
    session['activ'] = list()
    return redirect('/')

app.run(debug=True)
