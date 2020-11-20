


from flask import Flask, Response ,json, request
app = Flask(__name__)


# this json can be exported to a json file and imported and read  

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})







@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
              <p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def readinternaljson():
    return json.dumps(data)


@app.route('/readjson', methods=['GET'])
def readjsonfile():
     
    with open('sample-python.json', 'r') as f:
    	info = json.loads(f.read())
    return json.dumps(info)
    
    
@app.route('/writejson', methods=['GET', 'POST'])
def writejsonfile():
     
    with open('sample-write.json', 'w') as f:
    	info = json.dumps(f.write(b'{"text": "success"}' )); f.flush()
    return json.dumps(info)


if __name__ == '__main__':
    app.run(threaded=True, port=5001, debug=True, use_reloader=True)
