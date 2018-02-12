import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='wicshacks/build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
	if(path == ""):
		return send_from_directory('wicshacks/build', 'index.html')
	else:
		if(os.path.exists("wicshacks/build/" + path)):
			return send_from_directory('wicshacks/build', path)
		else:
			return send_from_directory('wicshacks/build', 'index.html')


if __name__ == '__main__':
	app.run(use_reloader=True, port=5000, threaded=True)
