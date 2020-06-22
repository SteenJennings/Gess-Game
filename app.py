from flask import Flask, render_template

app = Flask(__name__) #Flask variable called 'app'. Used in procfile

@app.route('/')
def yup():
    return render_template("index.html")
