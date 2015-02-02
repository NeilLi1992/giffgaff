#-*- coding:utf-8 -*-
from flask import Flask, g, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return "Hello, world! - Flask\n"

if __name__ == "__main__":
    app.run()
else:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
