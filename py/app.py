from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

USER_FILE = 'users.txt'

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as file:
        users = {}
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
        return users

def save_user(username, password):
    with open(USER_FILE, 'a') as file:
        file.write(f'{username}:{password}\n')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['username']
    email = request.form['password']
    password = request.form['password']
    users = load_users()
    if username in users:
        return 'Username already exists'
    save_user(username, password)
    return 'Signup successful'

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    users = load_users()
    if username not in users or users[username] != password:
        return 'Invalid username or password'
    return 'Signin successful'

@app.route('/')
def index():
    return render_template('signup_signin.html')

if __name__ == '__main__':
    app.run(debug=True)