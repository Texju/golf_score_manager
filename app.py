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
    cur = db.execute('select firstname, lastname, stableford from players order by id asc')
    entries = [dict(firstname=row[0], lastname=row[1], stableford=row[1]) for row in cur.fetchall()]
    return jsonify(tasks=entries)

@app.route('/players/new', methods=['POST'])
def new_player():
    db = get_db()
    cur = db.execute('insert into players (firstname,lastname,stableford,sex) values (?, ?, ?, ?)',
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
    cur = db.execute('select * from golfs order by id asc')
    entries = [dict(firstname=row[0], lastname=row[1], stableford=row[1]) for row in cur.fetchall()]
    return jsonify(tasks=entries)

@app.route('/golfs/new', methods=['POST'])
def new_golf():
    db = get_db()
    cur = db.execute('insert into golfs (name,slope,sss,handicap_hole_1,handicap_hole_2,handicap_hole_3,handicap_hole_4,handicap_hole_5,handicap_hole_6,handicap_hole_7,handicap_hole_8,handicap_hole_9,handicap_hole_10,handicap_hole_11,handicap_hole_12,handicap_hole_13,handicap_hole_14,handicap_hole_15,handicap_hole_16,handicap_hole_17,handicap_hole_18,par_hole_1,par_hole_2,par_hole_3,par_hole_4,par_hole_5,par_hole_6,par_hole_7,par_hole_8,par_hole_9,par_hole_10,par_hole_11,par_hole_12,par_hole_13,par_hole_14,par_hole_15,par_hole_16,par_hole_17,par_hole_18) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
               [request.json['name'],request.json['slope'],request.json['sss'],request.json['handicap_hole_1'],request.json['handicap_hole_2'],request.json['handicap_hole_3'],request.json['handicap_hole_4'],request.json['handicap_hole_5'],request.json['handicap_hole_6'],request.json['handicap_hole_7'],request.json['handicap_hole_8'],request.json['handicap_hole_9'],request.json['handicap_hole_10'],request.json['handicap_hole_11'],request.json['handicap_hole_12'],request.json['handicap_hole_13'],request.json['handicap_hole_14'],request.json['handicap_hole_15'],request.json['handicap_hole_16'],request.json['handicap_hole_17'],request.json['handicap_hole_18'],request.json['par_hole_1'],request.json['par_hole_2'],request.json['par_hole_3'],request.json['par_hole_4'],request.json['par_hole_5'],request.json['par_hole_6'],request.json['par_hole_7'],request.json['par_hole_8'],request.json['par_hole_9'],request.json['par_hole_10'],request.json['par_hole_11'],request.json['par_hole_12'],request.json['par_hole_13'],request.json['par_hole_14'],request.json['par_hole_15'],request.json['par_hole_16'],request.json['par_hole_17'],request.json['par_hole_18']])
    db.commit()
    id = cur.lastrowid
    return jsonify({
        "name" : request.json['name'],
        "slope" : request.json['slope'],
        "sss" : request.json['sss'],
        "handicap_hole_1" : request.json['handicap_hole_1'],
        "handicap_hole_2" : request.json['handicap_hole_2'],
        "handicap_hole_3" : request.json['handicap_hole_3'],
        "handicap_hole_4" : request.json['handicap_hole_4'],
        "handicap_hole_5" : request.json['handicap_hole_5'],
        "handicap_hole_6" : request.json['handicap_hole_6'],
        "handicap_hole_7" : request.json['handicap_hole_7'],
        "handicap_hole_8" : request.json['handicap_hole_8'],
        "handicap_hole_9" : request.json['handicap_hole_9'],
        "handicap_hole_10" : request.json['handicap_hole_10'],
        "handicap_hole_11" : request.json['handicap_hole_11'],
        "handicap_hole_12" : request.json['handicap_hole_12'],
        "handicap_hole_13" : request.json['handicap_hole_13'],
        "handicap_hole_14" : request.json['handicap_hole_14'],
        "handicap_hole_15" : request.json['handicap_hole_15'],
        "handicap_hole_16" : request.json['handicap_hole_16'],
        "handicap_hole_17" : request.json['handicap_hole_17'],
        "handicap_hole_18" : request.json['handicap_hole_18'],
        "par_hole_1" : request.json['par_hole_1'],
        "par_hole_2" : request.json['par_hole_2'],
        "par_hole_3" : request.json['par_hole_3'],
        "par_hole_4" : request.json['par_hole_4'],
        "par_hole_5" : request.json['par_hole_5'],
        "par_hole_6" : request.json['par_hole_6'],
        "par_hole_7" : request.json['par_hole_7'],
        "par_hole_8" : request.json['par_hole_8'],
        "par_hole_9" : request.json['par_hole_9'],
        "par_hole_10" : request.json['par_hole_10'],
        "par_hole_11" : request.json['par_hole_11'],
        "par_hole_12" : request.json['par_hole_12'],
        "par_hole_13" : request.json['par_hole_13'],
        "par_hole_14" : request.json['par_hole_14'],
        "par_hole_15" : request.json['par_hole_15'],
        "par_hole_16" : request.json['par_hole_16'],
        "par_hole_17" : request.json['par_hole_17'],
        "par_hole_18" : request.json['par_hole_18']})


if __name__ == '__main__':
    if os.path.exists(DATABASE):
        print("We found a database")        
    else : 
        print("First time ? We create database")
        init_db()
    app.run()

