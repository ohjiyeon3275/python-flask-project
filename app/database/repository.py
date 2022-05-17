import redis
import json

rd = redis.StrictRedis(host='localhost', port=6379, db=0)

rd.set('key', 'val')

