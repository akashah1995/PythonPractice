from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("indexlanding.html")
    return render_template("dojos.html")

@app.route('/ninjas')
def ninja():
    return render_template("ninja.html")

@app.route('/dojos/new')
def formfunction():
    return render_template("dojos.html")
    print "Got Post Info"
    name = request.form['name']

    
    return redirect('/')
app.run(debug=True) # run our server


