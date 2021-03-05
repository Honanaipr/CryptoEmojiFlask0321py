import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/encrypt.html')
@app.route('/index')
@app.route('/')
def encrypt():
    return render_template('encrypt.html')


@app.route('/decrypt.html')
def decrypt():
    return render_template('decrypt.html')
