import redis

from flask import Flask, render_template

from coffee.config import pool, app_config
from coffee.utils import json_response

app = Flask(__name__)
app.config.update(app_config)
r = redis.Redis(connection_pool=pool)


@app.route('/')
def index():
    return render_template('index.jinja2')


@app.route('/api/status')
def status():
    data = r.hgetall('coffeestatus')
    if len(data.keys()) == 0:
        return json_response({
            'coffee': {'status': 'unknown'}
        })

    return json_response({
        'coffee': data
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
