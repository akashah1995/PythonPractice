from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/')
def open():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/projects')
def myprojects():
    return render_template('projects.html')

app.run(debug=True) 

