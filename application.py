from flask import Flask, render_template, url_for, request, redirect,jsonify
from caption import *
import warnings
import base64
warnings.filterwarnings("ignore")



application = Flask(__name__)
@application.route('/', methods = ['POST','GET'])

def hello_world():
	if request.method == 'POST':
		data = request.get_json(force=True)
		image_data = data['image']
		imgdata = base64.b64decode(image_data)
		
		filename = 'static/something.jpg'
		with open(filename, 'wb') as f:
			f.write(imgdata)
			print("abc")
		
		caption = caption_this_image(filename)
		return jsonify({'description' : caption})
	
if __name__ == '__main__':
	application.run(debug = True)



