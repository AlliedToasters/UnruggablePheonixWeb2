from flask import Flask, request
import json
with open("./metadata.json", "r") as f:
    md = json.loads(f.read())

def get_metadata(id, md=md):
    if not 0 < int(id) < 889:
        return json.dumps({"error":"id is not between 1 and 888"})
    else:
        data = md[str(id)]
        data["image"] = "https://i.ibb.co/HCwP1Gz/pheonix-punk-sample.jpg"
        return json.dumps(md[str(id)])

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return 'Healthy!'

@app.route('/metadata')
def metadata():
    id = request.args.get('id')
    md = get_metadata(id)
    return md