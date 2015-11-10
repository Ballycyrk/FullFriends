from flask import Flask, flash, redirect, request, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'silvergold'
mysql = MySQLConnector('friendsdb')
@app.route('/')
def index():
  friends = mysql.fetch('SELECT * FROM friends')
  return render_template('index.html', friends = friends)

@app.route('/friends', methods=['POST'])
def create():
  first = request.form['first']
  last = request.form['last']
  job = request.form['occupation']
  insert = "INSERT INTO friends \
                (first_name, last_name, occupation, created_at, updated_at)\
            VALUES ('{}','{}','{}', NOW(), NOW())".format(first, last, job)
  mysql.run_mysql_query(insert)
  return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
  friend = mysql.fetch('SELECT * FROM friends WHERE id={}'.format(id))
  return render_template('friends.html', friend = friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
  first = request.form['first']
  last = request.form['last']
  occupation = request.form['occupation']
  update = "UPDATE friends \
            SET first_name='{}',last_name='{}',occupation='{}',updated_at= NOW()\
            WHERE id={}".format(first, last, occupation, id)
  mysql.run_mysql_query(update)
  return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
  delete = "DELETE FROM friendsdb.friends WHERE id = {}".format(id)
  mysql.run_mysql_query(delete)
  return redirect('/')
app.run(debug=True)
