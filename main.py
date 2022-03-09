from flask import Flask, render_template
from flask import abort
from datetime import datetime
import app.main.view as View
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'it is SECRET.'
bootstrap = Bootstrap(app)

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
    return render_template('user.html', name=name, current_time=datetime.utcnow)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route("/form", methods=["GET", "POST"])
def form_post():
    name = None
    form = View.NameForm()
    if form.validate_on_submit():
        name = form.name.data # empty name value changed to submitted value
        form.name.data='' # to empty form
    return render_template('form.html', form=form, name=name)