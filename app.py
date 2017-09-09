from flask import Flask, render_template, request, jsonify, _app_ctx_stack
from sqlite3 import dbapi2 as sqlite3
import os.path


DATABASE = './db/database.db'
DEBUG = True
SECRET_KEY = 'some super secret development key'

app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('./db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    db = get_db()
    cur = db.execute('select firstname, lastname, stableford from database order by id asc')
    entries = [dict(firstname=row[0], lastname=row[1], stableford=row[1]) for row in cur.fetchall()]
    return jsonify(tasks=entries)

@app.route('/players/new', methods=['POST'])
def new_player():
    db = get_db()
    cur = db.execute('insert into database (firstname,lastname,stableford,sex) values (?, ?, ?, ?)',
               [request.json['firstname'], request.json['lastname'], request.json['stableford'], request.json['sex']])
    db.commit()
    id = cur.lastrowid
    return jsonify({"firstname": request.json['firstname'],
                    "lastname": request.json['lastname'],
                    "stableford": request.json['stableford'],
                    "sex": request.json['sex'],
                    "id": id})

@app.route('/golfs')
def golfs():
    db = get_db()
    cur = db.execute('select * from database order by id asc')
    entries = [dict(firstname=row[0], lastname=row[1], stableford=row[1]) for row in cur.fetchall()]
    return jsonify(tasks=entries)

@app.route('/golfs/new', methods=['POST'])
def new_golf():
    db = get_db()
    cur = db.execute('insert into database (firstname,lastname,stableford,sex) values (?, ?, ?, ?)',
               [request.json['firstname'], request.json['lastname'], request.json['stableford'], request.json['sex']])
    db.commit()
    id = cur.lastrowid
    return jsonify({"firstname": request.json['firstname'],
                    "lastname": request.json['lastname'],
                    "stableford": request.json['stableford'],
                    "sex": request.json['sex'],
                    "id": id})

if __name__ == '__main__':
    if os.path.exists(DATABASE):
        print("We found a database")        
    else : 
        print("First time ? We create database")
        init_db()
    app.run()

