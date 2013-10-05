import redis 

from web.config import properties
from web.model import Issue, Commit

redis_connection = redis.StrictRedis(host=properties.get('REDIS_HOST'), port=int(properties.get('REDIS_PORT')))


def retrieve_view(key, start=0, stop=4):
    return map(lambda x: obj_from_key(x), redis_connection.lrange(key, start, stop))

def records(key):
    a = []
    for item in redis_connection.keys(key):
        a.append(obj_from_key(item))
    return a

def obj_from_key(key):
    if "issue:" in key or "pull:" in key:
        return Issue().from_dict(redis_connection.hgetall(key))
    if "commit:" in key:
        return Commit().from_dict(redis_connection.hgetall(key))


