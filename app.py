from flask import Flask render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!'

@app.route('/new')
def my_func():
	a = 2+3
	a = str(a)
	return a
	#pass
@app.route('/ray')
def my_func2():
	x = "ray says hi"
	x = x + '\n and have a good day\n jknsdjnsdj'
	#x = x + "/n"
	x = x + "thank you"
	return x


if __name__ == '__main__':
   app.run(debug=True)