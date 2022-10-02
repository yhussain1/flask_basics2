from flask import Flask
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix = "/admin")

@app.route("/")
def test():
    return "<h1>test</h1>"

if __name__ == "__main__":
    app.run(debug=True)