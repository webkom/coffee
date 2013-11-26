from flask import Flask, render_template

from coffee.config import app_config
from coffee.utils import json_response
from coffee.models import Status

app = Flask(__name__)
app.config.update(app_config)
status = Status()


@app.route('/')
def index():
    return render_template('index.jinja2')


@app.route('/api/status')
def api_status():
    try:
        status.get()
    except KeyError:
        return json_response({
            'coffee': {'status': 'unknown'}
        })

    return json_response({
        'coffee': status.to_dict()
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
