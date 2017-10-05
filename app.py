from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "password"
    
@app.route("/")
def welcome():
        session['username'] = "admin"
        return render_template('welcome.html')

@app.route("/logged_in") 
def logged_in():
        if 'username' in session:
                return render_template('logged_in.html', username = request.args['username'])
        else:
                return render_template('logged_in.html')
        session.pop("username")


if __name__ == "__main__":
    app.debug = True
    app.run()

