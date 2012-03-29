import json
import urllib2 as api

class APIRequest:
	"""
	Class to generate JSON request for the api
	"""
	def __init__(self, url, data):
		"""
		Initialize the dict
		"""
		REQUEST_HEADER = 'Content-Type', 'application/json;charset=UTF-8'
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
		request = api.urlopen(self.getURL())
		print self.getURL(), " =============> ", request.getcode()
