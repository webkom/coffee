from flask import Flask, render_template
from datetime import datetime

from coffee.config import app_config
from coffee.utils import json_response, txt_response
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


@app.route('/coffee.txt')
def coffeetxt():
    status.get()
    return txt_response('%(count)s\n%(date)s' % {
        'count': status.get_count(datetime.now()),
        'date': status.last_start.strftime('%d. %B %Y %H:%M:%S')
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
