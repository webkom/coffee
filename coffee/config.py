import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read([os.path.dirname(os.path.dirname(__file__)) + '/.coffeerc'])

app_config = {
    'DEBUG': config.getboolean('coffee_server', 'debug'),
    'REDIS_DB': int(config.get('coffee_server', 'redis_db')),
    'REDIS_HOST': config.get('coffee_server', 'redis_host'),
    'REDIS_PORT': int(config.get('coffee_server', 'redis_port')),
}
try:
    app_config['REDIS_PW'] = config.get('coffee_server', 'redis_pw')
except ConfigParser.NoOptionError:
    app_config['REDIS_PW'] = None
