# importing
from flask import Flask, render_template, request

# interaction
app = Flask(__name__)

# mapping
@app.route('/')
@app.route('/register')
# inputs
def register():
    return render_template("register.html")

# mapping
@app.route('/confirm', methods = ['POST','GET'])
# inputs
def confirm():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phonenumber')
        return render_template("confirmation.html",name=n , city = c, phonenumber = p)

# main

if __name__ == '__main__':
    app.run()
