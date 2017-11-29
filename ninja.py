from flask import Flask, render_template, request, redirect
app = Flask(__name__)
theuser=""

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("ninjanone.html")

@app.route('/ninja')
def allninja():
    return render_template("ninjaall.html")

# @app.route('/ninja/blue')
# def ninjablue():
#     return render_template("ninjablue.html")

# @app.route('/ninja/red')
# def ninjared():
#     return render_template("ninjared.html")

# @app.route('/ninja/purple')
# def ninjapurple():
#     return render_template("ninjapurple.html")

# @app.route('/ninja/orange')
# def ninjaorange():
#     return render_template("ninjaorange.html")

@app.route('/ninja/<vararg>')
def handler_function(vararg):
  print vararg
  if vararg == 'red':
      return render_template("ninjared.html")

  elif (vararg == 'blue'):
      return render_template("ninjablue.html")

  elif (vararg == 'purple'):
      return render_template("ninjapurple.html")

  elif(vararg == 'orange'):
      return render_template("ninjaorgane.html")

  else:
      return render_template("notapril.html")


      


    



app.run(debug=True)
