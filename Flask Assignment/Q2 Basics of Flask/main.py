from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=False)