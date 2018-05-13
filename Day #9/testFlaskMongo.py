from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://pytest:test@ds237848.mlab.com:37848/first'
app.config['MONGO_DB_NAME'] = 'first'

mongo = PyMongo(app)

@app.route('/add')
def add():
    users = mongo.db.users
    users.insert({'name':'Admin','password':'password'})
    return 'User added succefully'

if __name__ == '__main__':
    app.run(debug=True)