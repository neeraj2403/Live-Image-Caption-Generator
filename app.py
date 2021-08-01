from flask import Flask, render_template, url_for, request, redirect,jsonify
from caption import *
import warnings
import base64
warnings.filterwarnings("ignore")
import os
import time

app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])

def hello_world():
	if request.method == 'POST':
		data = request.get_json(force=True)
		image_data = data['image']
		imgdata = base64.b64decode(image_data)
	
		
		filename = 'something.jpg'
		filename = os.path.relpath(filename)
		with open(filename, 'wb') as f:
			f.write(imgdata)
			print("abc")
		caption = caption_this_image(filename)
		# time.sleep(5)

		return jsonify({'description' : caption})
	elif request.method == 'GET':
		return jsonify({'message':'sucess'})


if __name__ == '__main__':
	app.run(debug = True)



