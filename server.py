from flask import Flask, flash, redirect, request, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'silvergold'
mysql = MySQLConnector('friendsdb')
@app.route('/')
def index():
  friends = mysql.fetch('SELECT * FROM friends')
  return render_template('index.html', friends = friends)

@app.route('/friends')
def create():
  pass

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
  print '*********************In edit!', id
  return redirect('friends/' +str(id))

@app.route('/friends/<id>')
def update(id):
  print '!!!!!!!!!!!!!!!IN SHOW!!!!!!!!!!!!', id
  return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
  print '*******************IN DELETE**************************'
  return redirect('/')
app.run(debug=True)
