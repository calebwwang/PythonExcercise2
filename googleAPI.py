import os
import sys
import urllib2
from bottle import route, run, get, post, request
import HTML

url = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyDYyZCC32BnqauGRprJlB1c4fPSpx6Wym0&country=US&q=digital+camera&alt=json"
key = "AIzaSyDYyZCC32BnqauGRprJlB1c4fPSpx6Wym0"
output = urllib2.urlopen(url).read()
jsonData = json.loads(output)
print output


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
    output = urllib2.urlopen(url).read()
    print url



# Setup the local server
run(host='localhost', port=8080, debug=True)

