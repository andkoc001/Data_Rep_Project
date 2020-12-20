#!flask/bin/python

# Title: Data Representation Project, GMIT, 2020
# Author: Andrzej Kocielski; email: G00376291@gmit.ie, https://github.com/andkoc001/
# Description: Web App that consumes external API. The application is based on the lecture materials, and other sources quoted as they were used in the program.
# GitHub: https://github.com/andkoc001/Data_Rep_Project
# Lecturer: Dr. Andrew Beatty
####################################


# -------------------------------------
# Import external modules and databases
# -------------------------------------


# import git # temporarily disabled
from flask import Flask, jsonify, request, abort, make_response, render_template, session, redirect, url_for, g
from static.zequipmentDAO import equipmentDAO
import json

app = Flask(__name__, static_url_path='', static_folder='.')
app.secret_key = 'secretkeythatonly77shouldknow'


# ----------------
# Initial data for testing
# ----------------

# local stored data
""" equipment=[
    {"id": 1, "category": "Tier 1", "name":"CNC 2000",
        "supplier":"CNC machines Ltd", "price_eur":25762.50, "price_bc": null},
    {"id": 2, "category": "Tier 1", "name":"Las-Weld-Super",
        "supplier":"Weld Masters", "price_eur":16543.00, "price_bc": null},
    {"id": 3, "category": "Spare", "name":"Scanner RFID",
        "supplier":"Ocularify", "price_eur":499.99, "price_bc": null},
    {"id": 4, "category": "Tier 2", "name":"Deburr Cleaner",
        "supplier":"Weld Masters", "price_eur":899.00, "price_bc": null},
    {"id": 5, "category": "Tier 1", "name":"Conveyer 500x100", "supplier":"Line Optim", "price_eur":`12850.00, "price_bc": null},
] """

# -----------
# Login, based on https://youtu.be/2Zz97NVbH0U
# -----------


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(username='Andrzej', password='password'))
users.append(User(username='gmit', password='gmit'))
users.append(User(username='Gundolf', password='typefriendandenter'))


# -----------
# Flask routs - login
# -----------


# @app.before_request
# def before_request():
#     session.clear()
#     # session.pop('username', None)


@app.route('/loginold')
def loginold():
    return '<h1> login </h1> ' +\
        '<button>' +\
        '<a href="'+url_for('proccess_login')+'">' + 'login' + '</a>' +\
        '</button>'


@app.route('/', methods=['GET', 'POST'])
def home():
    # session['username'] = "gmit"
    # session.pop('username', None)
    if not 'username' in session:
        # return "inside home()1" # test ok
        return render_template('index.html')

    # return 'welcome ' + session['username'] # test ok
    return render_template('equipment.html')


@app.route('/accessdenied', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do stuff when the form is submitted
        session.pop('username', None)

        username = request.args.get('username', request.form['username'])
        password = request.args.get('password', request.form['password'])

        # username = request.form['username']
        # password = request.form['password']

        username = str(username)
        # return "inside login()1 - " + username # test ok
        if (username == "gmit") and (password == "gmit"):
            session['username'] = username
            # return "inside accessdatabase() 3"  # test ok
            return redirect(url_for('accessdatabase', username=username))

    # return "inside login()2" # test ok
    return render_template('equipment.html')


@ app.route('/accessdatabase/<username>', methods=['GET', 'POST'])
def accessdatabase(username):
    # return "inside accessdatabase() 1"  # test ok
    # check credentials
    #     return render_template('equipment.html')

    # # show the form, it wasn't submitted
    # # return "inside accessdatabase() 4"  # test ok
    # session.pop('username', None)
    return render_template('equipment.html')


@ app.route('/login3', methods=['GET', 'POST'])
def login3():
    if request.method == 'POST':
        print(request.form['username'])

    return '''
        <form method="POST"> Name: <input name="username" type="text">
        <input type="submit">
        </form>
    '''


@ app.route('/processlogin')
def proccess_login():
    # check credentials # if bad redirect to login page again
    if username == gmit and password == gmit:
        session['username'] = username

    # else
    # session['username'] = "gmit"
    return redirect(url_for('home'))


@ app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@ app.route('/data')
def getData():
    if not 'username' in session:
        abort(401)
    return '{"data":"all here"}'


# -----------
# Flask routs - data management
# -----------


@ app.route('/equipment')
def getAll():
    # session['username'] = "I dunno"
    if not 'username' in session:
        abort(401)
    # check in not zequipmentDAO.getAll() <- with 'z' before equipment
    results = equipmentDAO.getAll()
    return jsonify(results)

# ---- get by id ----
# @app.route('/equipment/<int:id>', methods=['GET'])


@ app.route('/equipment/<int:id>')
def findById(id):
    session['username'] = "I dunno"
    if not 'username' in session:
        abort(401)

    foundEquipment = equipmentDAO.findByID(id)
    # Check if id exists
    if not foundEquipment:
        return "That id not found in the database"
        abort(404)

    # foundEquipment = list(filter(lambda t: t['id'] == id, equipment))
    # if len(foundEquipment) == 0:
    #     return jsonify({'equipment': ''}, indent=4), 204
    # foundEquipment = equipmentDAO.findByID(id)
    return jsonify(foundEquipment)
    # return jsonify({'equipment': foundEquipment[0]})

# ---- create ----


@ app.route('/equipment', methods=['POST'])
def create():
    if not 'username' in session:
        abort(401)

    # check if exist
    if not request.json:
        return "Wrong request"
        abort(400)
    # if not 'id' in request.json:
        # return "Wrong request (id)"
        # abort(400)

    equip = {
        "category": request.json['category'],
        "name": request.json['name'],
        "supplier": request.json['supplier'],
        "price_eur": request.json['price_eur']
    }
    # Make the tuple for DB
    values = (equip['category'], equip['name'],
              equip['supplier'], equip['price_eur'])
    newId = equipmentDAO.create(values)  # possibly with 'z' before equipment
    equip['id'] = newId
    # return jsonify(equipment)
    # equipment.append(equip)
    return jsonify(equip)
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"category":"Tier 2","name":"Fiatto","supplier":"Puntto","price_eur":30.00}' http://localhost:5000/equipment
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"category\":\"Tier 2\",\"name\":\"Fiatto\",\"supplier\":\"Puntto\",\"price_eur\":30.00}" http://localhost:5000/cars


# ---- update ----
@ app.route('/equipment/<int:id>', methods=['PUT'])
def update(id):
    if not 'username' in session:
        abort(401)

    foundEquipment = equipmentDAO.findByID(id)
    if not foundEquipment:
        return "That id not found in the database"
        abort(404)
    if not request.json:
        return "Wrong request"
        abort(400)
    reqJson = request.json

    # checks for data integrity
    '''
    if ('price_eur' in reqJson) and (type(reqJson['price_eur']) is not float):
        abort(400)
        return "Wrong request or data type (should be float)"
    '''
    if 'category' in request.json:
        foundEquipment['category'] = reqJson['category']
    if 'name' in request.json:
        foundEquipment['name'] = reqJson['name']
    if 'supplier' in request.json:
        foundEquipment['supplier'] = reqJson['supplier']
    if 'price_eur' in request.json:
        foundEquipment['price_eur'] = reqJson['price_eur']

    # Make the tuple for DB
    values = (foundEquipment['category'], foundEquipment['name'],
              foundEquipment['supplier'], foundEquipment['price_eur'], foundEquipment['id'])
    # Do the update on DB
    equipmentDAO.update(values)

    return jsonify(foundEquipment)
# curl -i -H "Content-Type:application/json" -X PUT -d '{"name":"Fiesta"}' http://localhost:5000/equipment/5
# for windows use this one
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Fiesta\"}" http://localhost:5000/equipment/5


@ app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_car(id):
    if not 'username' in session:
        abort(401)

    foundEquipment = equipmentDAO.findByID(id)
    if not foundEquipment:
        return "That id does not exist in the database"
        abort(404)
    equipmentDAO.delete(id)
    return jsonify({"done": True})


# --------------------------------
# Error handling with Flask routes
# --------------------------------

# disabled for debugging purposes
'''
@app.errorhandler(404)
def not_found404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_found400(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
'''

# -------------------------------
# GitHub with PythonAnywhere sync
# -------------------------------
# Based on: https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664

# disabled temporarily - more testing needed
'''
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/andkoc001/Data_Rep_Project')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
'''

# ------------------
# Check dependencies
# ------------------

if __name__ == '__main__':
    app.run(debug=False)
