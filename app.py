import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

from utils import transform
from utils import ocr_api


app = Flask(__name__)
ALLOWED_EXTENSIONS = set([ 'pdf'])
app.config['UPLOAD_FOLDER'] = os.path.join('api','uploads')

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		full_filename =  os.path.join(app.config['UPLOAD_FOLDER'], filename)       
		file.save(full_filename)
		jpgs_dirpath = transform.fileTransformAPI(full_filename, filename)
		text = ocr_api.jpegToTextAPI(jpgs_dirpath)
		print('текст распознан')
		resp = jsonify({'message' : f'File: {filename} successfully uploaded ', 'text': text})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


if __name__ == '__main__':
    app.run(port=5000,debug=True, host="0.0.0.0")