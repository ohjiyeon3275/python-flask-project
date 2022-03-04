from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def index():
    request.get_data()
    return "<h1>Hi!</h1>"

app.add_url_rule('/', 'index', index) # == @app.route("/index")


@app.route("/user/<name>", methods=["GET"])
def user(name):
    return "hello {}".format(name)

# @app.route("/redirect", methods=["GET"])
# def redirect():
#     return redirect('http://github.com/ohjiyeon3275')

#what is this function and __things__ for
if __name__ == '__main__':
    app.run