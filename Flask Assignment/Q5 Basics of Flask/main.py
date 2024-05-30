from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
# Configure secret key for sessions
app.config['SECRET_KEY'] = 'supersecretkey'

# Configure session to use filesystem (alternatively, you can use Redis, Memcached, etc.)
app.config['SESSION_TYPE'] = 'filesystem'
users = {
    'arush.james': '123'
}
@app.route('/')
def home_page():
    if 'username' in session:
        return f"Hello {session['username']}! <a href='/logout'>Logout</a>"
    return f"You are not logged in.<br><a href='/register'>Register</a><br> <a href='/login'>Login</a>"
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]==password:
            session['username'] = username
            return redirect('/')
        else:
            return f"Password is wrong or User doesnt exist"
    return render_template('login.html')
@app.route('/logout',methods=['GET', 'POST'])
def logout():
    session.pop('username',None)
    return redirect('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return f"This user name already exists!<a href='/register'>Try Again</a>"
        users[username] = password
        redirect('/login')
    return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)
