from flask import Flask ,request,jsonify,render_template,send_file
import os
from flask_cors import CORS

from plugs.app_manger import *
from plugs.filename_gen import filename_gen
from plugs.volume_increser import inc_vol

UPLOAD_FOLDER = "./temp"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.before_request
def del_spek():
    clear_all_speak()


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

        return jsonify(resp)
    return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
      </form>
      '''

@app.route("/api/speak/",methods=['POST','GET'])
def speak():
    file = request.args.get("file")
    return send_file(file)

@app.route("/test",methods=['POST','GET'])
def test():
    if request.method == 'POST':
        file = request.files['file']
        file.save("test.wav")
        # print(file)
    return "200"

@app.route("/testapp",methods=['POST','GET'])
def testapp():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(port=2002,debug=True,host="0.0.0.0")