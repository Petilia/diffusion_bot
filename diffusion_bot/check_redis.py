import redis

# host = "redis://:diffusion_bot@redis"
host = "redis"
# host = "localhost"

r = redis.Redis(
    host=host, 
    password="password"
)

r.set("dsdsds", "dsdsd")

print("all ok")