from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/java')
def java():
    return render_template('java.html')

@app.route('/cpp')
def cpp():
    return render_template('cpp.html')


if __name__=='__main__':
    app.run(debug=False)