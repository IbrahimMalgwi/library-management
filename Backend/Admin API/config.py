import redis

class Config:
    MONGO_URI = "mongodb://localhost:27017/library_admin"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

redis_client = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)
