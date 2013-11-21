import redis

from flask import Flask, request, render_template

from config import pool, app_config
from utils import json_response

app = Flask(__name__)

app.config.update(app_config)

r = redis.Redis(connection_pool=pool)

if __name__ == "__main__":
    app.run()
