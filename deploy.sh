#First remove node_modules folder
sls plugin install -n serverless-wsgi
sls plugin install -n serverless-add-api-key
sls plugin install -n serverless-python-requirements
sls deploy