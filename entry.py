from backend.main import app as backend
import os

from flask import Flask
app = Flask(__name__)
app.register_blueprint(backend)

if __name__ == '__main__':
    port = 8080
    if "PORT" in os.environ:
        port = os.environ["PORT"]

    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=port, debug=True)
    # [END gae_python37_app]