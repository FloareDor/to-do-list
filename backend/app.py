from __future__ import print_function
import sys
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

#app.config["MONGO_URI"] = "mongodb://localhost:27017/visipedia_annotation_toolkit"
#mongo = PyMongo(app)

with open("data.json", "w") as outfile:
	json.dump({"todo": [], "done": []}, outfile)

@app.route("/")
def main():
	return "Hello"

@app.route('/api/addtodo', methods=['POST', 'GET'])
def add_todo():
	# x.headers.add('Access-Control-Allow-Origin', '*')
	
	print("received something", file=sys.stderr)
	todo = request.json['todo']
	print(todo , file=sys.stderr)
	json_data = {}
	with open('data.json', 'r') as openfile:
		json_data = json.load(openfile)
		json_data["todo"].append(todo)
	openfile.close()
	with open('data.json', 'w') as openfile: 
		json.dump(json_data, openfile)
	openfile.close()
	print(todo)
	return jsonify({'message': 'Todo added successfully'})

@app.route('/api/getdata', methods=['POST', 'GET'])
def get_todo():
	try:
		with open('data.json', 'r') as openfile:
			json_data = json.load(openfile)
			print(json_data , file=sys.stderr)
			return jsonify(json_data)
	except Exception as e:
		print(e , file=sys.stderr)

@app.route('/api/adddone', methods=['POST', 'GET'])
def add_done():
	print("received something", file=sys.stderr)
	index = request.json["index"]
	done = request.json['done']
	print(done , file=sys.stderr)
	json_data = {}
	with open('data.json', 'r') as openfile:
		json_data = json.load(openfile)
		if index>0:
			json_data["todo"].pop(index-1)
		json_data["done"].append(done)
	openfile.close()
	with open('data.json', 'w') as openfile: 
		json.dump(json_data, openfile)
	openfile.close()
	print(done)
	return jsonify({'message': 'Done added successfully'})

@app.route('/api/clear', methods=['POST', 'GET'])
def clear():
	with open('data.json', 'w') as openfile:
		json.dump({"todo": [], "done": []}, openfile)
	openfile.close()
	return jsonify({'message': 'Data cleared successfully'})

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)