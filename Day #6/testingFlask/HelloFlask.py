from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html', title='Hello template')

@app.route('/result', methods=['POST'])
def result():
    first = request.form['first']
    second = request.form['second']
    operation = request.form['operation']
    result = ''
    result = first + operation + second
    result = eval(result)
    return render_template('result.html', result=result)
app.run(debug=True)