# import dependencies
import os
from flask import Flask
import json

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    VCAP_APPLICATION = json.loads(os.environ['VCAP_APPLICATION'])

    return 'Welcome to Nimbus! container ID: %s' %(VCAP_APPLICATION["application_id"])


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
