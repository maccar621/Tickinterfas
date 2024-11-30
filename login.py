from flask import Flask, render_template, request, redirect, url_for, session

login = Flask(__name__)
login.secret_key ='tu clave_secreta_aqui'

users = {}

@login.route('/index1')
def index1():
    user = session.get('user')
    if user:
        return f"Bienvenido,  {user}!!!"
    return "Bienvenido a la aplicacion de registro de usuarios"

@login.route(rule='/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
        users[username] = password
        print(users)
        return redirect('index1')
    return render_template('register.html')
@login.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index1'))

if __name__ == '__main__':
    login.run(debug=True)