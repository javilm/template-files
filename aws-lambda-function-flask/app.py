from flask import Flask, request, jsonify
import awsgi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify(msg='hello')

@app.route('/get/', methods=['GET'])
def get():
    return jsonify(msg=request.args.get('msg'))

@app.route('/post/', methods=['POST'])
def post():
    return jsonify(msg=request.form['msg'])

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

