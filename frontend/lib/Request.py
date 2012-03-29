import json
import urllib, urllib2

class APIRequest:
	"""
	Class to generate JSON request for the api
	"""
	REQUEST_HEADER = {'Content-Type':'application/json;charset=UTF-8'}

	def __init__(self, url, data):
		"""
		Initialize the dict
		"""
		self.setURL(url)
		self.setData(data)

	def setURL(self, url):
		"""
		Sets the request url
		"""
		self.url = url
	
	def getURL(self):
		"""
		Gets the request url
		"""
		return self.url


	def setData(self, data):
		"""
		Sets the request data
		"""
		self.data = data
	
	def getJSON(self):
		"""
		Gets the request data in JSON format
		"""
		return json.dumps(self.data)

	def getResponse(self):
		"""
		Makes the request, validates and returns a response
		"""
		req = urllib2.Request(self.getURL(), data=urllib.urlencode(self.data),
				 headers=self.REQUEST_HEADER)
		opener = urllib2.OpenerDirector()
		opener.add_handler(urllib2.HTTPHandler())
		opener.add_handler(urllib2.HTTPDefaultErrorHandler())
		f = opener.open(req)
		import json
		print json.load(f)
		
