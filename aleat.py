#!/usr/bin/python3

import webapp

class URLaleat(webapp.webApp):
	def process(self, parsedRequest):
		import random
		return("200 OK", "<html><body><h1>Hola. <a href =" + str(random.randint(1, 1000000)) + ">Dame otra </a></p></body></html>")
		
if __name__ == "__main__":
	testWebApp = URLaleat('localhost', 1234)

