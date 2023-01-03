import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'hello world'

@app.route('/item/new', methods=['POST'])
def add_item():
    req_data=request.get_json()
    item = req_data['item']

    res_data= helper.addlist(item)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')

        return response
    response = Response(json.dumps(res_data),mimetype='application/json')
    return response

@app.route('/item/all', methods=['GET'])
def getalll():
    res_data=helper.getall()
    response = Response(json.dumps(res_data),mimetype='application/json')
    return response 

@app.route('/item/status', methods=['GET'])
def getitem():
    item_name = request.args.get('name')
    status = helper.getitem(item_name)
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response
@app.route('/item/update',methods=['PUT'])
def update():
    req_data= request.get_json()
    item = req_data['item']
    status= req_data['status']
    res_data= helper.update_status(item , status)

    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response 
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/item/delete',methods=['DELETE'])
def delete():
    req_data=request.get_json()
    item= req_data['item']
    res_data= helper.delete(item)

    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
        return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response
if __name__ == '__main__':
    app.run(host="0.0.0.0")
