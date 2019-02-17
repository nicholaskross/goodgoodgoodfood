from backend.main import app as backend
import os

from flask import Flask, send_from_directory, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(backend)

dist_base = "goodgoodwebpage/dist/goodgoodwebpage"


@app.route("/")
def send_index():
    return send_file(dist_base + "/index.html")


@app.route("/<path:path>")
def send_static(path):
    return send_from_directory(dist_base, path)


if __name__ == '__main__':
    port = 8080
    if "PORT" in os.environ:
        port = os.environ["PORT"]

    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=port, debug=True)
    # [END gae_python37_app]
