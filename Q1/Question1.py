from flask import Flask, url_for
app = Flask(__name__)

@app.route('/<string:name>')
def hello(name):
	
	if name.isalpha() == False:
		newname = ""
		for element in name:
			if element.isalpha() == True:
				newname = newname + element
		return "<h1> Welcome, "+ newname + ", to my CSCB20 Website </h1>" 
	
	if name.isupper() == True:
		return "<h1> Welcome, "+ name.lower() + ", to my CSCB20 Website </h1>"
	if name.islower() == True:
		return "<h1> Welcome, "+ name.upper() + ", to my CSCB20 Website </h1>"

if __name__ == "__main__":
	app.run(debug=True)
