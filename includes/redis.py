import redis
import json
import settings

class Cache:
    _client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

    @staticmethod
    def get(key):
        val = Cache._client.get(key)
        return json.loads(val) if val else None

    @staticmethod
    def set(key, value, ttl=600):
        Cache._client.setex(key, ttl, json.dumps(value))