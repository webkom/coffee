import ConfigParser

from redis import ConnectionPool


config = ConfigParser.ConfigParser()
config.read(['.coffeerc'])

pool = ConnectionPool(
    db=config.get('coffee_server', 'redis_db'),
    host=config.get('coffee_server', 'redis_host'),
    port=int(config.get('coffee_server', 'redis_port'))
)

app_config = {
    'DEBUG': config.getboolean('coffee_server', 'debug')
}
