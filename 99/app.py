from flask import Flask
from flask import request
import requests
import sys
app = Flask(__name__)

ID = '99'
NUM = 99
NEXT_ADDR = 'serv132:5003'

@app.route('/')
def send():
	global ID
	global NUM
	global NEXT_PORT
	param = request.args.get('token')
	token = int(param)
	
	if (param == ID): # my ID == received token
		print('['+ ID + '] ' + 'I\'m leader Now!', file=sys.stderr) # Leader selected, stop GET loop
		return ''
	elif(token < NUM): # my ID > received token
		try:
			response = requests.get('http://' + NEXT_ADDR + '/?token=' + ID) # send my ID for token
		except requests.exceptions.RequestException as e:
			print('\n Cannot reach the service. \n', file=sys.stderr)
			return 'ERROR\n'
	else: # (my ID < received token) or (my ID == received token)
		try:
			response = requests.get('http://' + NEXT_ADDR + '/?token=' + param) # send received token
		except requests.exceptions.RequestException as e:
			print('\n Cannot reach the service. \n', file=sys.stderr)
			return 'ERROR\n'
	return ''
	
if __name__ == "__main__":
	global MY_PORT
	app.run(host = '0.0.0.0', port = 5002, debug = True)
