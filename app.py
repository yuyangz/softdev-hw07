from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/")
def welcome():
    #session.pop[request.args['username']]
    return render_template('welcome.html')

@app.route("/logged_in") 
def logged_in():
    app.secret_key = "user1" 
    session[app.secret_key] = "chicken"
    for x in session:
        print x
    return render_template('logged_in.html', username = request.args['username']) 

if __name__ == "__main__":
    app.debug = True
    app.run()

