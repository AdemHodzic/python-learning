from flask import Flask, render_template, request, session, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://pytest:test@ds237848.mlab.com:37848/first'
app.config['MONGO_DB_NAME'] = 'first'

mongo = PyMongo(app)


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({"name": "Admin"})
        if(login_user['name'] == request.form['username']):
            if(login_user['password'] == request.form['password']):
                session['name'] =  login_user['name']
                return redirect(url_for('home'))
            else:
                return "Wrong password"
        else:
            return "Username doesn't exist"
    else:
        if 'name' in session:
            temp_list=getCheckList()
            return render_template('list.html', 
                username=session['name'],
                check_list=temp_list['list'])
        return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        register_user = users.find_one({"name": request.form['username']})
        if register_user:
            return "Username already taken"
        else:
            name = request.form['username']
            password = request.form['password']
            users.insert({'name': name, 'password': password})
            session['name'] = name
            return redirect(url_for('home'))
    else:
        return render_template('register.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        text = request.form['text']
        duration = request.form['duration']
        lists = mongo.db.lists
        lists.update(
            {"name":session['name']},
            {
                '$push': 
                {'list':
                    {
                        "name":text,
                        "duration":duration,
                        "is_done":"false"
                    }
                }
            }
            )
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/delete',methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        lists = mongo.db.lists
        text = request.form['text']
        
        lists.update(
            {"name":session['name']},
            {
                '$pull':{'list':{"name":text}}
            }
        )

        return redirect(url_for('home'))
    else:
        return render_template('delete.html')

def getCheckList():
    lists = mongo.db.lists
    check_list = lists.find_one({"name":"Admin"})
    return check_list

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
