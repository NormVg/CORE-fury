from flask import Flask ,request,jsonify
import os

from plugs.app_manger import *
from plugs.filename_gen import filename_gen
from plugs.volume_increser import inc_vol

from flask_cors import CORS
UPLOAD_FOLDER = "./temp"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/')
def index():
    return '<-- thefury core system -->'

@app.route("/fury",methods=['POST','GET'])
def fury():
    if request.method == 'POST':
        file = request.files['file']
        name = filename_gen(".wav")
        file_save = os.path.join(app.config['UPLOAD_FOLDER'], name)
        file.save(file_save)
        file_save ,name_ = inc_vol(file_save)
        
        # FURY PROCESSING START
        resp = fury_init(file_save)
        print(resp)
        # clearing the temp
        clear_temp(name)
        clear_temp(name_)
        return resp
    return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
      </form>
      '''

if __name__ == "__main__":
    app.run(port=2002,debug=True)