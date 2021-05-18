from flask import Flask, render_template, url_for, request, redirect,jsonify
from caption import *
import warnings
import base64
warnings.filterwarnings("ignore")



app = Flask(__name__)


# @app.route('/')
# def hello():
#     return render_template('index.html')


@app.route('/', methods = ['POST','GET'])

def hello_world():
	if request.method == 'POST':
		data = request.get_json(force=True)
		image_data = data['image']
		imgdata = base64.b64decode(image_data)
		
		# for show
		# from PIL import Image
		# import io
		# image = Image.open(io.BytesIO(imgdata))
		# image.show()
		
		# save image
		filename = 'static/something.jpg'
		with open(filename, 'wb') as f:
			f.write(imgdata)
			print("abc")
		
		caption = caption_this_image(filename)
		# result_dic = {
		# 		# 'image' : "Server/static/" + img.filename,
		# 		'description' : caption
		# 	}

		return jsonify({'description' : caption})
	




# def upload_file():
# 	if request.method == 'POST':
# 		img = request.files['image']

# 		# print(img)
# 		# print(img.filename)

# 		img.save("Server/static/"+img.filename)

	
# 		caption = caption_this_image("Server/static/"+img.filename)



		
# 		result_dic = {
# 			'image' : "Server/static/" + img.filename,
# 			'description' : caption
# 		}
# 	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)