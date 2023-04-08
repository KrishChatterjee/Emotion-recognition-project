import librosa # for audio file analysis
import librosa.display #to explicitly set the location of each object
from glob import glob # to list out all files in directory
import matplotlib.pyplot as plt #for plotting
import numpy as np  # to work with vector arrays
import speaker_verification_toolkit.tools as svt
from sklearn.mixture import GaussianMixture as GMM
import pickle as cPickle 



import model
import likelihood
import os
from flask import Flask, render_template,request, url_for,redirect,flash
from werkzeug.utils import secure_filename
from pathlib import Path
from flask import send_from_directory
import re


UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = {'wav'}
app = Flask(__name__)            #Initialize the flask App
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "abc"




@app.route('/')
def home():
    return render_template('base.html')




@app.route('/train',methods=['GET'])
def train():
    return render_template('train.html')







@app.route('/train/<int:no>',methods=['GET', 'POST'])
def train_upload(no):
    if request.method == 'POST':
        name=request.form['name']
        files = request.files.getlist("model")

        for file in files:
            file_name=file.filename
            full_file= os.path.basename(file_name)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], full_file))

        model.func2(no,name)
        flash("Model saved!!!")

        for file in files:
            file_name=file.filename
            full_file= os.path.basename(file_name)
            os.remove(os.path.join('./upload/'+full_file))

        return render_template('download.html',name=name)
    
    return render_template('train_post.html',no=no)





@app.route('/download/<name>',methods=['GET', 'POST'])
def download(name):
    uploads = os.path.join(app.root_path)
    return send_from_directory(directory=uploads,path=name,as_attachment=True)










def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS















@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':

        file = request.files['emotion']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)                 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path=likelihood.func()
            pattern = '[\w-]+?(?=\.)'
            a = re.search(pattern, file_path)
            emotion=a.group()
            flash(f"The Emotion is {emotion}")
            os.remove(os.path.join('./upload/'+filename))
        


    return render_template('test.html')



if __name__ == "__main__":
    app.run(debug=True)