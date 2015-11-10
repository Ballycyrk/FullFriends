from flask import Flask, flash, redirect, request, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'silvergold'
mysql = MySQLConnector('friendsdb')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/friends')
def create():
  pass

@app.route('/friends/<id>/edit')
def edit(id):
  pass

@app.route('/friends/<id>')
def update(id):
  pass

@app.route('/friends/<id>/delete')
def destroy(id):
  pass
app.run(debug=True)
