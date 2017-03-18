from flask import Flask, render_template, redirect, url_for, request
import json

#configuration
DATABASE = 'vmwsssp.json'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_page', methods=['POST'])
def user_page():
    LanID = request.form['LanID'].strip()
    if LanID == 'pkeertip':
        return render_template('userpage.html')


if __name__ == "__main__":
    app.run(debug=True)