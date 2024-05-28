#!/usr/bin/env python
# -*- coding:utf-8 -*-

__version__ = "1.3.0"

def main():
	print("{0}/{1}".format(__name__, __version__))
	print("--------------------------------")
	print("Example:")
	print("{0} --server YOUR-SERVER --apikey YOUR-APIKEY --method YOUR-METHOD --query YOUR-QUERY".format(__name__))
	
	import argparse
	parser = argparse.ArgumentParser(description="{0}".format(__name__))
	parser.add_argument("-s", "--server", action="store")
	parser.add_argument("-k", "--apikey", action="store")
	parser.add_argument("-m", "--method", action="store")
	parser.add_argument("-q", "--query", action="store")
	
	args = parser.parse_args()
	
	try:
		def to_string(s1):
			if s1 is not None:
				return ("{0}".format(s1)).strip()
				pass
			return ""
			pass
		
		params = {}
		params["server"] = to_string(args.server)
		params["apikey"] = to_string(args.apikey)
		params["method"] = to_string(args.method)
		params["query"] = to_string(args.query)
		
		print("--------------------------------")
		for i in params.keys():
			print("{0}: {1}".format(i, params[i]))
			pass
		print("--------------------------------")
		
		import socket
		socket.setdefaulttimeout(10)
		
		import urllib.parse
		
		url = params["server"]
		data = "query={0}".format(urllib.parse.unquote_plus(params["query"]))
		data = data.encode("UTF-8")
		
		headers = {
			"User-Agent": "",
			"Content-Type": "application/x-www-form-urlencoded",
			"X-APIKEY": urllib.parse.unquote_plus(params["apikey"]),
		}
		
		import json
		import urllib.request
		
		request = urllib.request.Request(url, data, headers, method="POST")
		response = urllib.request.urlopen(request)
		body = response.read().decode("UTF-8")
		
		import random
		import hashlib
		s1 = to_string(random.random())
		hash1 = hashlib.sha256(s1.encode()).hexdigest()[:6]
		path1 = "lib{0}.{1}.py".format(__name__, hash1)
		
		try:
			with open(path1, "w", encoding="UTF-8") as f:
				f.write(body)
				pass
			
			import importlib
			import importlib.util
			spec = importlib.util.spec_from_file_location("{0}.{1}".format(__name__, hash1), path1)
			obj1 = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(obj1)
			
			import os
			if os.path.exists(path1):
				os.remove(path1)
				pass
			
			obj1.main(params)
			del obj1
			pass
		except:
			import traceback
			print(traceback.format_exc())
			pass
		
		import os
		if os.path.exists(path1):
			os.remove(path1)
			pass
		
		pass
	except:
		import traceback
		print(traceback.format_exc())
		pass
	
	print("--------------------------------")
	print("END")
	pass

if __name__ == "__main__":
	main()
	pass
