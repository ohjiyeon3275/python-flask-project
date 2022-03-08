from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

def index():
    return "<h1>Hi!</h1>"
app.add_url_rule('/', 'index', index) # == @app.route("/index")


@app.route("/user/<name>", methods=["GET"])
def user(name):
    if name == 'usererror':
        abort(500)
    return "hello {}".format(name)


@app.route("/render-user/<name>", methods=["GET"])
def user_render(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
