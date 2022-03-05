from flask import Flask, render_template, request, redirect
from flask import abort

app = Flask(__name__)

def index():
    request.get_data()
    return "<h1>Hi!</h1>"

app.add_url_rule('/', 'index', index) # == @app.route("/index")


@app.route("/user/<name>", methods=["GET"])
def user(name):
    if name == 'usererror':
        abort(404)
    return "hello {}".format(name)

@app.route("/render-user/<name>", methods=["GET"])
def user_render(name):
    return render_template('template/user.html', name=name)



#what is this function and __things__ for
if __name__ == '__main__':
    app.run