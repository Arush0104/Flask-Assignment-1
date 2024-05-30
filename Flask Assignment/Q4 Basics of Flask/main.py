from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['GET'])
def page():
    data = request.args.get('user_input')
    return render_template('res.html', user_data = data)


if __name__=='__main__':
    app.run(debug=False)