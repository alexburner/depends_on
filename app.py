import os

from flask import Flask
from redis import Redis

PORT = int(os.getenv("PORT", 8080))

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"


@app.route('/health/<src>')
def health(src):
    msg = f"Health {src}"
    print(msg)
    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
