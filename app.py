import pymysql
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def create_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Abcdefg123!",
        # DATABASE
        cursorclass=pymysql.cursors.DictCursor
    )

app.run(debug=True)