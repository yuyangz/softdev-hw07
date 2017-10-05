from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "password"
    
@app.route("/")
def welcome():
        if 'user1' in session:
                return render_template('logged_in.html', username = 'user1')
        else:
                return render_template('welcome.html')

@app.route("/logged_in") 
def logged_in():
        if (request.args['username'] == 'user1' and request.args['password'] == 'admin'):
                session['user1'] = "admin"
                return render_template('logged_in.html', username = request.args['username'])
        else:
                return render_template('error.html')


@app.route("/logged_out")
def logged_out(): 
        session.pop("user1")
        return render_template('welcome.html')



if __name__ == "__main__":
    app.debug = True
    app.run()

