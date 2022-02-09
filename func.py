import requests
import json

headers = {"Content-Type": "application/json; charset=utf-8",
			'X-Tasktest-Token' : 'token'}



def get_status(message):
	
	
	res = requests.get("https://dev.wapp.im/v3/instance"+ message["id"] + "/status?"
												 + "phone=" + message["phone"] ,
												 headers=headers, data=json.dumps(message), timeout = 30)
	return res

def send_message(message):	

	res = requests.post("https://dev.wapp.im/v3/instance"+ message["id"] + "/sendMessage?phone=" + message["phone"]+
												"&body=" + message["body"] + "&token=" + message["token"],
												headers=headers, data=json.dumps(message), timeout = 30)

	return res



def req_chat(url,data):



	response = requests.get("https://dev.wapp.im/v3/chat/spare?crm=TEST&domain=test",
											 data=json.dumps(data), headers=headers, timeout = 30)
	return response


def create_chat(data):
	


	response = requests.get("https://dev.wapp.im/v3/instance" 
											+ data["id"] + "/status?full=1&token=" + data["token"],
											 data=json.dumps(data), headers=headers, timeout = 30)
	return response


def get_chat(message):
	response = requests.get("https://dev.wapp.im/v3/instance" + message["chat_id"] + "/readChat?token=" 
											+ message["token"] + "&chatId=" + message["chat_id"], 
											data=json.dumps(message), headers=headers, timeout = 30)
	return response



def quit(message):
	response = requests.get("https://dev.wapp.im/v3/instance" + message["id"] + "/logout?token=" + message["token"], 
															headers=headers)
	return response