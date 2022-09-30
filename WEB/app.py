from urllib import request
import os
import pandas as pd
import seaborn as sns
import numpy as np
import os
from flask import Flask, flash,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

PEOPLE_FOLDER = os.path.join('static', 'imgaes')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def index():
    
    
    
    full_filename1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Graph1.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Graph2.png')
    full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'Graph3.png')
    full_filename4 = os.path.join(app.config['UPLOAD_FOLDER'], 'Graph4.png')
    return render_template("index.html", user_image1 = full_filename1, user_image2 = full_filename2, user_image3 = full_filename3, user_image4 = full_filename4,n = "lorem Ipsum " )

# @app.route('/')
# def sendVal():
#     return render_template('index.html', n = a)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/success/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'dataFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['dataFile']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))    
    data = pd.read_csv("titanic.csv")
    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h1>{{data}}</h1>
    '''


if __name__ == '__main__':
    app.run(debug = True)