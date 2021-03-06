from application import app
from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
import requests
import random
import os

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    sentence = response.text
    names= open("names.txt", "a")
    names.write(sentence)
    names.close
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/hero', methods=['GET', 'POST'])
def home_hero():
    response = requests.get('http://service_4:5003/randomword/hero')
    sentence = response.text
    names= open("names.txt", "a")
    names.write(sentence)
    names.close
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/villain', methods=['GET', 'POST'])
def home_villain():
    response = requests.get('http://service_4:5003/randomword/villain')
    sentence = response.text
    names= open("names.txt", "a")
    names.write(sentence)
    names.close
    return render_template('index.html', sentence = sentence, title = 'Home')

