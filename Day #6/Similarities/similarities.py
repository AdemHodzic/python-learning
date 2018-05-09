import os
from flask import Flask, render_template, request
import re

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

ALLOWED_EXTENSIONS = ['.txt']


def isAllowed(name: str)->bool:
    ext = ''
    for i in range(len(name)-4, len(name), 1):
        ext+=name[i]
    return ext in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    #try:
        if 'mainFile' not in request.files or 'secondFile' not in request.files:
            return render_template('error.html', error="File wasn't sent")

        mainFile = request.files['mainFile']
        secondFile = request.files['secondFile']

        if mainFile.filename == '' or secondFile.filename == '':
            return render_template('error.html', error="Empty name")

        if isAllowed(mainFile.filename) and isAllowed(secondFile.filename):
            main_file_string = str(mainFile.read()).replace('b','',1)
            second_file_string = str(secondFile.read()).replace('b','',1)
            main_file_string = re.sub(r'\r\n|\r|\n','\n', main_file_string)
            return render_template('results.html', mainFileString=main_file_string
            , secondFileString=second_file_string  )
        else:
            return render_template('error.html', eror="Wrong file format")
        
        return render_template('error.html', error="Failed to process the file")
    #except:
    #    return render_template('error.html', error="File is too large")
app.run(debug=True)
