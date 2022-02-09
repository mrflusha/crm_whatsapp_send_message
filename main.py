import requests
import json
from time import sleep
import webbrowser
import func




def unpack(resp):

	return json.loads(resp.text)




#[begin] get token, if need token uncoment all. need refacror this code
url = 'https://dev.wapp.im/v3/chat/spare?crm=TEST&domain=test'
 
headers = {"Content-Type": "application/json; charset=utf-8",
			'X-Tasktest-Token' : 'token'}
 
data = { "key" : "value"
}
 
response = requests.get(url, headers=headers, json=data)
print("Status Code", response)

chat = json.loads(response.text)
print(chat)
'''


try:
	if chat['error_text'] == "No free chats":
		print("wait free chats", chat['error_text'])
		while chat['error_text'] == "No free chats":
			response = func.req_chat(url,data)
			chat = json.loads(response.text)
			sleep(90)
			print(chat)
except KeyError as e:
	print(e)

'''
flie = "text.txt"

#with open(file,"w") as f:
	#f.write(chat_id,chat_token)

'''

chat_id = chat["id"]
chat_token = chat["chat_token"]


[end block]
'''
also = func.req_chat(response,data)
also = json.loads(also.text)
print(also)
chat_id = "24"
chat_token = "chat_token"
print(chat_id,chat_token,"\n"+str(chat))

#check connection state



me = requests.get("https://dev.wapp.im/v3/instance" + chat_id + "/status?full=1&token=" + chat_token, headers= headers, json=data)

me = unpack(me)

print(me)



#[begin] Get whats_app QR
data = {
	"id" : str(chat_id),
	"token" : chat_token,
	"accountStatus" : "got qr code"

}
print(data["id"],data["token"])

qr_code = func.create_chat(data)
acc_status = json.loads(qr_code.text)
acc_status = acc_status["accountStatus"]
print(acc_status)
if acc_status != 'authenticated':
	try:
		qr_code = json.loads(qr_code.text)["qrCode"]
	except KeyError as e:
		print(e)
		status = json.loads(qr_code.text)["accountStatus"]
		while status != data["accountStatus"]:
			try:
				print("wait QR")
				sleep(10)
				qr_code = func.create_chat(data)
				#staus = json.loads(qr_code.text)["status"]

				status = json.loads(qr_code.text)["accountStatus"]
				if status == data["accountStatus"]:
					qr_code = json.loads(qr_code.text)["qrCode"]
					break
			except KeyError as e:
				print(e)
				print(json.loads(qr_code.text))
				qr_code = json.loads(qr_code.text)["qrCode"]
				webbrowser.open(qr_code, new=1, autoraise=True)
			finally:
				print(status)



	webbrowser.open(qr_code, new=1, autoraise=True)

print(qr_code)
#[end block]



message = {
	"id" : str(chat_id),
    "phone": "79872745052",
    "body": "Hello, 🍏",
    "token" : chat_token,
    "chat_id" : "79872745052@c.us"
}


mew = input("press enter if QR code scaned")


msg_sended = func.send_message(message)
sts = func.get_status(message)

print(json.loads(msg_sended.text),"\n",json.loads(sts.text))

chat_history = func.get_chat(message)
chat_history = unpack(chat_history)


print(chat_history)

quit = func.quit(message)
quit = unpack(quit)
print(quit)