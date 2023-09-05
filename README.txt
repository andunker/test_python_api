python -m venv vEnv
pip install -r requirements.txt

______________________________________________________________________________________________________________________________

serverless create --template aws-python3 --path test-python-api

	
sls plugin install -n serverless-wsgi
sls plugin install -n serverless-add-api-key
sls plugin install -n serverless-python-requirements

serverless.yml ->

"""
service: test-python-api
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.11
plugins:
 - serverless-wsgi
 - serverless-python-requirements
custom:
 wsgi:
   app: app.app
   packRequirements: false
functions:
 app:
   handler: wsgi_handler.handler
   events:
     - http:
        path: /items
        method: get
     - http:
        path: /items/{id}
        method: get

package:
  patterns:
    - '!venv/**'
    - '!node-modules/**'

"""


run in local:
serverless wsgi serve

serverless deploy

serverless remove