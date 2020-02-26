from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import abort

app = Flask(__name__)

###in memory datastructure to store words and their count

word_count={}

###custom error handlers for status codes 404 and 405 (which are more likely to occur in this problem statement

@app.errorhandler(404)
def handle_bad_request(e):
	return  jsonify({"error":404,"description":"Enter the correct URL containing the parameter"})
@app.errorhandler(405)
def handle_bad_request(e):
	return jsonify({"error":405,"description":'Choose the correct HTTP methods'})


###main function to store the words and maintain their count 

@app.route("/word/<word>",methods=["GET","POST","DELETE"])
def func(word):
	if request.method == "POST":                                           #To increase count by one
		if(word in list(word_count.keys())):			       #if word already exists, increase its count
			word_count[word]=word_count[word]+1
			return "Word count increased"
		
		else:                                                          #word doesn't exist add it to dictionary with count 1
			word_count[word]=1
			return "Word added"

	elif request.method == "GET":                                          #to get the count of the word
		if(word in list(word_count.keys())):                           #if word present in dictionary return its count

			data = {word: word_count[word]}
			return jsonify(data)
		else:                                                          #if word not present return 0
			
			data = {word:0}
			return jsonify(data)
			

	elif request.method == "DELETE":                                       #To decrease count of a word by one
		word_count[word]=word_count[word]-1
		return "Word count decreased"
	
		

if (__name__ == "__main__"):
	try:
		app.run(port = 4000)                                           #port on which the server will run
	except:
		print ("run on different port")
