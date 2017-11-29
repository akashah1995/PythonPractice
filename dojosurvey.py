from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecretasfuck'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("dojosurvey.html")

@app.route('/survey', methods = ['POST'])
def survey():
    print "Got post info"
    theuser = request.form['your name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comment']
    if len(theuser) < 1:
        flash("The name field cannot be empty!")
        return redirect('/')
    elif len(comments) < 1:
        flash("The comment field cannot be empty!")
        return redirect('/')
    elif len(comments) > 120:
        flash("The comments field has too many characters")
        return redirect('/')
    else:
        return render_template("dojoinfo.html",user=theuser,location=location,language=language,comments=comments)

app.run(debug=True)
