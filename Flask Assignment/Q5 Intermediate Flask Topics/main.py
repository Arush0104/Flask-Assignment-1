from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my Flask app! "
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
