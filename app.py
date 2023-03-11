from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=["GET"])
def main_page():
    with open('main_page.html', 'r') as f:
        content = f.read()
    return Response(content, status=200, mimetype='text/html')

app.run(host='0.0.0.0')

