from ss import  screenshot
from flask import  Flask,render_template, send_file, request
from flask import *

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/screenshot_name',methods = ['POST'])
def save():
    global text
    text = request.form['test']
    return render_template('info_name.html')

@app.route('/take_screenshot',methods = ['GET'])
def download():
    screenshot(text)
    filename = text +'.png'
    return send_file(filename,as_attachment=True)

if __name__ == "__main__":
     app.run(debug=True)