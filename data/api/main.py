from flask import Flask, request, Response, json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>yoo</p>"

@app.route("/segments/download", methods=["POST"])
def segments_download():
    data = request.json
    
    return Response(status=200)


@app.route("/segments", methods=["GET"])
def get_segments():
    params = request.args
    test = {
        'hi': 'bye',
        'albert': 'bye',
        'url': 'http://randomfox.ca/floof'
    }
    return Response(json.dumps(test), status=200)
