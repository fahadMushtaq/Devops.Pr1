
#!/usr/bin/python
from flask import Flask

PORT = 8080
MESSAGE = """In the name of Allah.  
There is nothing more important than the Tawheed of Allah, and Worshipping Him alone.  With this I say: 
Hello, world, and I call you to Islam!\n"""

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=PORT)
