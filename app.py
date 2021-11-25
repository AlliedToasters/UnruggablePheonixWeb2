from flask import Flask, request, send_file, Response
import json

description = """
The Phoenix Punks is the first NFT collection made by the $WGMI (ERC-20) community. 
The collection consists of 888 unique Phoenix Punks, which represent how we, as a community, rose from the ashes after the token was initially rugged by its creator. 
All royalties from secondary sales of NFTs in this collection will be directed towards supplying liquidity for the $WGMI token, via purchasing ETH/WGMI LP tokens and locking that liquidity away forever by burning those LP tokens.
"""

with open("./metadata.json", "r") as f:
    md = json.loads(f.read())

def get_metadata(id, md=md):
    if not 0 < int(id) < 889:
        return json.dumps({"error":"id is not between 1 and 888"})
    else:
        data = md[str(id)]
        data["image"] = "https://i.ibb.co/N1jX58g/preview.gif"
        data["description"] = description
        data["name"] = "Pheonix Punk " + data["name"]
        return json.dumps(data)

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return 'Healthy!'

@app.route('/metadata')
def metadata():
    id = request.args.get('id')
    data = get_metadata(id)
    return Response(data, mimetype="application/octet-stream")