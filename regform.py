from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecretasfuck'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("regform.html")


@app.route('/register' , methods = ['POST'])
def register():

    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']
    if ((len(session['firstname']) < 1) or (len(session['lastname']) < 1) or (len(session['email']) < 1) or (len(session['password']) < 1) or (len(session['confirm']) < 1)):
        flash('All fields must be filled in!')
        return redirect('/')
    if (str.isalpha(str(session['firstname'])) == False) or (str.isalpha(str(session['lastname'])) == False):
        flash('First name and Last name fields can only contain letters!')
        return redirect('/')
    if not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    
    if (len(session['password']) < 8):
        flash('Password is too short!')
        return redirect('/')

    if session['password'] != session['confirm']:
        flash("Password fields do not match! ")
        return redirect('/')

    flash('Thank you for registering for this cause!')
    return render_template('submitted.html')

app.run(debug=True)

