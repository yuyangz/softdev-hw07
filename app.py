from flask import Flask, render_template, request, session


app = Flask(__name__)

@app.route("/")
def welcome():
    app.secret_key = "chicken"
    if (request.args('username') == "ham" and
        request.args('password') == app.secret_key):
        return render_template('welcome.html')

@app.route("/logged_in") 
def logged_in():
    return render_template('logged_in.html', username = request.args['username']) 

if __name__ == "__main__":
    app.debug = True
    app.run()

