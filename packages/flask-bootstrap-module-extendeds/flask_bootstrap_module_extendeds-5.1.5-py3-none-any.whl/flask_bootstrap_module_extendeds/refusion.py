from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from waitress import serve
import sqlite3

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret'

ADMIN_USERNAME = 'copp'
ADMIN_PASSWORD = 'password'

def create_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL,
                 full_name TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 email TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS applications
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER NOT NULL,
                 car_number TEXT NOT NULL,
                 description TEXT NOT NULL,
                 status TEXT DEFAULT 'Ожидает',
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('user_id', None)
    flash('Вы успешно вышли из аккаунта!', 'info')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        phone = request.form['phone']
        email = request.form['email']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, full_name, phone, email) VALUES (?, ?, ?, ?, ?)",
                  (username, password, full_name, phone, email))
        conn.commit()
        conn.close()
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Вход выполнен успешно!', 'success')
            return redirect(url_for('admin'))
        else:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
            user = c.fetchone()
            conn.close()
            if user:
                session['user_id'] = user[0]
                flash('Вход выполнен успешно!', 'success')
                return redirect(url_for('applications'))
            else:
                flash('Неверные логин или пароль!', 'danger')
    return render_template('login.html')

@app.route('/applications')
def applications():
    user_id = session.get('user_id')
    if user_id:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT applications.id, users.full_name, applications.car_number, applications.description, applications.status FROM applications JOIN users ON applications.user_id = users.id WHERE user_id = ?", (user_id,))
        applications = c.fetchall()
        conn.close()
        return render_template('applications.html', applications=applications)
    else:
        flash('Пожалуйста, авторизуйтесь для доступа к заявлениям!', 'info')
        return redirect(url_for('login'))


@app.route('/new_application', methods=['GET', 'POST'])
def new_application():
    if request.method == 'POST':
        car_number = request.form['car_number']
        description = request.form['description']
        user_id = session.get('user_id')
        if user_id:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("INSERT INTO applications (user_id, car_number, description) VALUES (?, ?, ?)",
                      (user_id, car_number, description))
            conn.commit()
            conn.close()
            flash('Заявление отправлено!', 'success')
            return redirect(url_for('applications'))
        else:
            flash('Пожалуйста, авторизуйтесь для отправки заявления!', 'info')
            return redirect(url_for('login'))
    return render_template('new_application.html')

@app.route('/admin')
def admin():
    if session.get('admin_logged_in'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT applications.id, users.full_name, applications.car_number, applications.description, applications.status FROM applications JOIN users ON applications.user_id = users.id")
        applications = c.fetchall()
        conn.close()
        return render_template('admin.html', applications=applications)
    return redirect(url_for('login'))

@app.route('/change_status/<int:application_id>', methods=['POST'])
def change_status(application_id):
    new_status = request.form['status']
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE applications SET status = ? WHERE id = ?", (new_status, application_id))
    conn.commit()
    conn.close()

    return redirect(url_for('admin'))


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8000)
