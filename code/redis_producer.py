import time
import argparse
import redis

DEFAULT_REDIS_HOST = "127.0.0.1"
DEFAULT_REDIS_PORT = 6379

parser = argparse.ArgumentParser(description='Redis producer')
parser.add_argument('--host',
                    dest='host',
                    type=str,
                    required=False,
                    help='Redis host (default {})'.format(DEFAULT_REDIS_HOST))
parser.add_argument('--port',
                    dest='port',
                    type=int,
                    required=False,
                    help='Redis port (default {})'.format(DEFAULT_REDIS_PORT))
args = parser.parse_args()
redis_host: str = args['host'] if args.__getattribute__('host') else DEFAULT_REDIS_HOST
redis_port: int = args['port'] if args.__getattribute__('port') else DEFAULT_REDIS_PORT

r = redis.Redis(host=redis_host, port=redis_port, db=1)

for i in range(100):
    r.rpush("test", "message #{}".format(i))
    time.sleep(1)

