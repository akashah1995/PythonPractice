from flask import Flask, render_template
  
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')

def helloworld():
    return render_template('index.html')

@app.route('/success')

def success():
  return render_template('success.html')

app.run(debug=True) 
     # Run the app in debug mode.

