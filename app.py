import os
from flask import Flask, render_template, redirect, url_for, request, g, json

DATABASE = 'db/vmwsssp.json'

app = Flask(__name__)

@app.before_request
def before_request():
    db = open(DATABASE).read()
    g.db = json.loads(db)
    
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        open(DATABASE, 'w').write(json.dumps(g.db))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage', methods=['POST'])
def user_page():
    LanID = request.form['LanID']
    users = g.db['a_users']
    machines = g.db[LanID]
    context = {'requester': LanID, 'machines': machines}
    if LanID in users:
        return render_template('userpage.html', **context)
    
@app.route('/vm', methods=['POST'])
def new_machine():
    requester = request.form['requester']
    enddate = request.form['date-input']
    available_vms = g.db['available_vms']
    pick_a_vm = available_vms[0]
    machinename = pick_a_vm['name']
    ipaddress = pick_a_vm['ipaddress']
    g.db[requester].insert(0, {
        'name':machinename,
        'ipaddress':ipaddress,
        'enddate':enddate
    })
    del available_vms[0]
    machines = g.db[requester]
    context = {'requester': requester, 'machines': machines}
    return render_template('userpage.html', **context)

if __name__ == "__main__":
    app.run(debug=True)