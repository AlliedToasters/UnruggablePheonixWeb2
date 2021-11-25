from flask import Flask, request
import json
with open("./metadata.json", "r") as f:
    md = json.loads(f.read())

def get_metadata(id, md=md):
    if not 0 < int(id) < 889:
        return json.dumps({"error":"id is not between 1 and 888"})
    else:
        return json.dumps(md[str(id)])

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return 'Healthy!'

@app.route('/metadata')
def metadata():
    id = request.args.get('id')
    return get_metadata(id)