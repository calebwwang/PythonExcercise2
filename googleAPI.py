import urllib2
import HTML
from bottle import route, run, get, post, request
#import HTML

# The prompt page where it asks for a players name
@route('/prompt')
def hello():
	# Read in the html file from the local directory
	f = open('prompt.htm')
	return f.read()
	f.close()


# The page where it displays the data
@post('/data')
def login_submit():
	# Replace spaces with + signs to insert into the url
	search = request.forms.get('name').replace(' ','+')
	url = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyDYyZCC32BnqauGRprJlB1c4fPSpx6Wym0&country=US&q="+search+"&alt=json"
	output = urllib2.urlopen(url).readlines()
	# Initialize the table
	table = [ ['Product Name', 'Price'] ]
	# parse the output
	# Look through each line for the data I want
	for index in range(len(output)):
		line = output[index]
		# Check for height data
		if line.count('"title":') > 0:
			title = getTitle(line)
		if line.count('"price":') > 0:
			price = getPrice(line)
			temp = [title, price]
			table.append(temp)
		# Package the data
	print table
	# Turn the python list into an html text table
	htmlTable = HTML.table(table)
	outFile1 = open('output1.htm')
	outFile2 = open('output2.htm')
	return outFile1.read() + htmlTable + outFile2.read()
	outFile1.close()
	outFile2.close()


# get title function
def getTitle(line):
	line = line.strip()
	temp = line.split(' ',1)[1]
	temp = temp.strip(',')
	temp = temp.strip('"')
	return temp

# get price function
def getPrice(line):
	line = line.strip()
	temp = line.split(' ',1)[1]
	temp = temp.strip(',')
	temp = temp.strip('"')
	temp = '$'+temp
	if temp[-2] == '.':
		temp = temp + '0'
	return temp


# Setup the local server
run(host='localhost', port=8080, debug=True)
