from flask import Flask, render_template, request, Session


app = Flask(__name__)

    
@app.route("/")
def welcome():   
        return render_template('welcome.html')

@app.route("/logged_in") 
def logged_in():
  Session['username'] = 'admin' #ERROR
  app.secret_key = "password"
  Session['password'] = app.secret_key #ERROR
  if (request.args('username') == Session['username'] and request.args('password') == Session['password']):
      return render_template('logged_in.html', username = request.args['username'])

if __name__ == "__main__":
    app.debug = True
    app.run()

