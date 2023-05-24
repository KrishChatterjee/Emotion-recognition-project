



import model
import likelihood
import os
from flask import Flask, render_template,request, url_for,redirect,flash,send_from_directory
from werkzeug.utils import secure_filename
import re
from pathlib import Path
from multiprocessing import Process
from threading import Thread

#Initialize the flask App and sets up configurations for file uploads and secret key.
app = Flask(__name__)            
UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = {'wav'}
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
    return send_from_directory(directory=uploads,path=name,as_attachment=True ,environ=request.environ)



    








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