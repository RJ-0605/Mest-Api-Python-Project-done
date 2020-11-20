
import pymongo 
from flask import Flask, Response ,json
app = Flask(__name__)

@app.route('/')
def base():

    try :
    	
    	response = json.dumps({"Status": "UP"})	
    	status=200
    	print (response)	
    except Exception as e:
    	response = json.dumps(Exception)
    	status=500
    finally:	
    	return Response(response ,
                    status,
                    mimetype='application/json')
                    
                    
                    
                    
                    
  
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
